import os
import requests
from dotenv import load_dotenv
from flight_data import FlightData
from pprint import pprint

# SECURITY: Load API key
load_dotenv("../.env")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("kiwi_flight_key")


class FlightSearch:
    """Searches flight data via Kiwi.com API.

    Handles both direct flights and flights with stopovers.
    Gracefully falls back to stopovers if direct flights unavailable.
    """

    def get_destination_code(self, city_name):
        """Convert city name to IATA airport code."""
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Search for cheapest flight between two cities.

        First tries direct flights (max_stopovers=0).
        If none found, retries with stopovers allowed (max_stopovers=1).

        Returns:
            FlightData: Cheapest flight found, or None if no flights available
        """
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,  # Start with direct flights only
            "curr": "GBP"
        }

        # API: Search for direct flights
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        # PATTERN: Try direct flights first, fall back to stopovers
        try:
            data = response.json()["data"][0]  # Direct flight found
        except IndexError:
            # No direct flights; try with stopovers allowed
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)

            # PATTERN: With stopovers, route has 3 legs: [outbound, stopover, return]
            # route[0] = departure city -> stopover city
            # route[1] = stopover city (unused but present)
            # route[2] = stopover city -> destination city
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],  # After stopover
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]  # City where stopover occurs
            )
            return flight_data
        else:
            # Direct flight found
            # PATTERN: With direct flight, route has 2 legs: [outbound, return]
            # route[0] = departure -> destination
            # route[1] = destination -> departure
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data

