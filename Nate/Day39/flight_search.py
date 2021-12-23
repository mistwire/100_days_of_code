import requests
# from flight_data import FlightData

KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "yhNAAqSaDKTjQI1ZsVAi6ZnCOYiYOyCp"


class FlightSearch:

    def search_flight(self, flight_data):
        # flight_data = FlightData()
        query = {
            "fly_from": flight_data.fly_from,
            "fly_to": flight_data.fly_to,
            "dateFrom": flight_data.dateFrom,
            "dateTo": flight_data.dateTo,
            "return_from": flight_data.return_from,
            "return_to": flight_data.return_to,
            "curr": "USD"
        }
        headers = {"apikey": API_KEY}
        response = requests.get(url=f'{KIWI_ENDPOINT}/v2/search', params=query, headers=headers)
        return response.json()

    def get_destination_code(self, city):
        headers = {"apikey": API_KEY}
        query = {
            "term": city,
            "location_type": "city"
        }
        response = requests.get(url=f'{KIWI_ENDPOINT}/locations/query', params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['locations'][0]['code']
