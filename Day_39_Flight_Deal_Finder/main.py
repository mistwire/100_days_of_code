from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# PATTERN: Multi-class architecture - each class has single responsibility
data_manager = DataManager()                    # Manages Google Sheet (Sheety API)
sheet_data = data_manager.get_destination_data()  # Fetch list of destinations to monitor
flight_search = FlightSearch()                  # Searches flights (Kiwi.com API)
notification_manager = NotificationManager()   # Sends SMS alerts (Twilio API)

# Configuration
ORIGIN_CITY_IATA = "BOS"  # Boston Logan - origin for all flights

# PATTERN: Initialize data on first run
# Google Sheet might not have IATA codes initially; populate them
if sheet_data[0]["iataCode"] == "":
    # Convert city names to IATA codes via Kiwi.com location API
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # Update local copy
    data_manager.destination_data = sheet_data
    # Update Google Sheet so we don't re-fetch next run
    data_manager.update_destination_codes()

# PATTERN: Define date range for flight search
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# PATTERN: Loop over destinations and check for deals
for destination in sheet_data:
    # Kiwi.com API: search for cheapest flight to this destination
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # PATTERN: Threshold-based alert
    # Only notify if price dropped below previous low
    if flight.price < destination["lowestPrice"]:
        # Send SMS with flight details
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )



