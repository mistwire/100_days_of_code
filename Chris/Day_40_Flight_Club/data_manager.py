import os
import requests
from dotenv import load_dotenv
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/users/sheet1"
load_dotenv("../.env")
sheety_token = os.getenv("sheety_workout_token")
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

