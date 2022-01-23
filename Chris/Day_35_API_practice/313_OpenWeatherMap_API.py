import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(".env")
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("api_key")
print(api_key)
# Use environment variables to keep them out of github
# http://twil.io/secure
# good primer on environment variables and .env files https://www.twilio.com/blog/environment-variables-python

account_sid = os.getenv("account_sid")
print(account_sid)
auth_token = os.getenv("auth_token")
print(auth_token)

rainy_place = {
    "lat": 31.608013,
    "lon": -84.335167,
    "appid": api_key,
}

parameters = {
    "lat": 43.023979,
    "lon": -70.913673,
    "appid": api_key,
}

response = requests.get(url=weather_endpoint, params=rainy_place)
response.raise_for_status()
print(f"status code: {response.status_code}")

data = response.json()['hourly']
is_raining = False
for i in range(12):
    if data[i]['weather'][0]['id'] < 700:
        is_raining = True
if is_raining:
    # print("Bring an ☂️")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                body="It's going to rain today. Bring an ☂️",
                from_='+16075245651',
                to='+16034988677'
            )
    print(message.status)


