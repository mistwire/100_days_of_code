import requests
from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = "AC9f71e683a403031c1c5a6dc4ec10959a"
MY_LAT = 47
MY_LONG = -53
open_weather_key = "f83bda1d52d74dba4cfb9c0e922b89f1"
url = "https://api.openweathermap.org/data/2.5/onecall"
city_name = "Amesbury"
MY_TWILIO_NUMBER = "+15304831979"
MY_NUMBER = "+13039173568"


def send_twilio_msg(message):
    account_sid = os.environ[TWILIO_ACCOUNT_SID]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=message,
                         from_=MY_TWILIO_NUMBER,
                         to=MY_NUMBER
                     )

    print(message.sid)


def get_weather_data():
    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": open_weather_key,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(url=url, params=params)
    response.raise_for_status()

    return response.json()

# for index, hour in enumerate(data['hourly']):
#     if index < 12:
#         for weather in hour['weather']:
#             if weather['id'] < 600:
#                 print("Bring an umbrella")
#             elif weather['id'] < 700:
#                 print("It's going to snow")
# for hour in hourly_data:
#     for weather in hour['weather']:
#         if weather['id'] < 600:
#             print("Bring an umbrella")
#         elif weather['id'] < 700:
#             print("It's going to snow")


data = get_weather_data()
hourly_data = data['hourly'][:12]
will_rain = False

for hour in hourly_data:
    for weather in hour['weather']:
        if weather['id'] < 600:
            will_rain = True

if will_rain:
    send_twilio_msg("Bring an umbrella.")
else:
    print("It's not going to rain.")

