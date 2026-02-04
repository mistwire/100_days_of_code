import os
import requests
from dotenv import load_dotenv
from pprint import pprint

# API: Sheety - Google Sheets REST API
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/flightDeals/prices"

# SECURITY: Load credentials from .env
load_dotenv("../.env")
sheety_token = os.getenv("sheety_workout_token")

# PATTERN: Custom header for Bearer token authentication
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}


class DataManager:
    """Manages data persistence via Google Sheets (via Sheety API).

    Handles reading destination list and updating IATA codes.
    Separates data layer from business logic (flight search, notifications).
    """

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Fetch all destinations from Google Sheet.

        Returns:
            list: Destination data with columns: city, iataCode, lowestPrice, id
        """
        # API: GET request to Sheety endpoint
        # Sheety translates this to: "Read 'prices' sheet from 'Flight Deals' spreadsheet"
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]  # Extract 'prices' array from response

        # Pretty-print for debugging (pprint formats dict readably)
        pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        """Update Google Sheet rows with IATA codes.

        Called after populate IATA codes via flight API.
        Uses PUT request to update each row individually.
        """
        for city in self.destination_data:
            # Sheety expects nested structure: {"price": {"iataCode": "BOS"}}
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # API: PUT request updates row by ID
            # city['id'] is unique identifier from Google Sheets (auto-assigned by Sheety)
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers,
            )
            print(response.text)
