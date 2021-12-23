import requests

SHEETY_API = ""
SHEETY_PUT_API = "


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            json = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PUT_API}/{city['id']}", json=json)
            response.raise_for_status()

