from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Configuration
ORIGIN_CITY_IATA = "LON"  # London - origin for all flights

# PATTERN: Multi-class architecture (see Day 39)
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Fetch destination list from Google Sheet
sheet_data = data_manager.get_destination_data()

# PATTERN: Populate IATA codes if missing
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# PATTERN: Dictionary comprehension for fast lookups
# Convert list of dicts to dict of dicts, keyed by IATA code
# Original: [{"iataCode": "DEN", "city": "Denver", "lowestPrice": 150, ...}]
# Result: {"DEN": {"id": 2, "city": "Denver", "price": 150}, ...}
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

# Date range for flight search
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# PATTERN: Loop over destinations and check for deals
for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)

    # PATTERN: Skip if no flights found (None check)
    if flight is None:
        continue

    # PATTERN: Threshold-based alert
    if flight.price < destinations[destination_code]["price"]:
        # Fetch all subscribers from Google Sheet
        users = data_manager.get_customer_emails()
        # Extract emails and names for notification
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        # Build notification message
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        # PATTERN: Conditional message enrichment
        # Add stopover information if applicable
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # PATTERN: Generate Google Flights booking link
        # Format: https://www.google.com/flights?#flt={depart_airport}.{arrive_airport}.{date}*{return}
        # Users can click to book immediately
        link = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        # PATTERN: Bulk notifications to multiple users
        # Each subscriber gets personalized email
        notification_manager.send_emails(emails, message, link)


