import os
import requests
from dotenv import load_dotenv
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/flightDeals/prices"
load_dotenv("../.env")
sheety_token = os.getenv("sheety_workout_token")
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers,
            )
            print(response.text)
