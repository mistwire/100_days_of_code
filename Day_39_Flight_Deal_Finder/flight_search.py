import os
import requests
from dotenv import load_dotenv
from flight_data import FlightData

# SECURITY: Load API key from .env
load_dotenv("../.env")

# API: Kiwi.com Tequila flight search API
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("kiwi_flight_key")


class FlightSearch:
    """Searches flight data via Kiwi.com API.

    Handles city name to IATA code conversion and flight price searches.
    Returns FlightData objects for price comparison and display.
    """

    def get_destination_code(self, city_name):
        """Convert city name to IATA airport code.

        Args:
            city_name: City name (e.g., "Boston", "London")

        Returns:
            str: IATA code (e.g., "BOS", "LON")
        """
        # Kiwi.com locations API endpoint
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        query = {
            "term": city_name,           # Search term (city name)
            "location_types": "city"     # Return cities, not individual airports
        }
        # API: GET request to location search
        r = requests.get(url=location_endpoint, headers=headers, params=query)
        results = r.json()["locations"]  # Extract locations array
        code = results[0]['code']         # Get IATA code of first result
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Search for cheapest flight between two cities in date range.

        Args:
            origin_city_code: Departure IATA code (e.g., "BOS")
            destination_city_code: Arrival IATA code (e.g., "DEN")
            from_time: datetime for earliest departure
            to_time: datetime for latest departure

        Returns:
            FlightData: Cheapest flight found, or None if no flights available
        """
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            # PATTERN: Format dates in Kiwi.com format (DD/MM/YYYY, European style)
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            # Trip parameters
            "nights_in_dst_from": 7,     # Minimum stay at destination
            "nights_in_dst_to": 28,      # Maximum stay at destination
            "flight_type": "round",      # Round-trip only
            "one_for_city": 1,           # One result per destination (cheapest)
            "max_stopovers": 0,          # Direct flights only (no layovers)
            "curr": "USD"                # Currency
        }

        # API: Search for flights
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        # PATTERN: Handle missing data gracefully
        try:
            data = response.json()["data"][0]  # Get first (cheapest) flight
        except IndexError:
            # No flights found for this route
            print(f"No flights found for {destination_city_code}.")
            return None

        # PATTERN: Extract nested flight data from API response
        # response structure: {"data": [{"route": [{...}, {...}], "price": 300}]}
        # route[0] = outbound leg (departure city -> destination city)
        # route[1] = return leg (destination city -> departure city)
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],      # Departure city name
            origin_airport=data["route"][0]["flyFrom"],    # Departure airport code
            destination_city=data["route"][0]["cityTo"],   # Arrival city name
            destination_airport=data["route"][0]["flyTo"], # Arrival airport code
            # Extract date from ISO timestamp (e.g., "2024-02-04T10:30:00" -> "2024-02-04")
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

