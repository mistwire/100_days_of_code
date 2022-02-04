import os
import requests
from dotenv import load_dotenv
from pprint import pprint


load_dotenv("../.env")

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("kiwi_flight_key")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/flightDeals/prices"
sheety_token = os.getenv("sheety_workout_token")

sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
headers = {
    "apikey": TEQUILA_API_KEY,
}

query = {
    "fly_from": "BOS",
    "fly_to": "DEN",
    "date_from": "01/02/2022",
    "date_to": "01/07/2022",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "USD"
}

r = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)

pprint(r.json())


