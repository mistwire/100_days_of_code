import requests
import datetime as dt

MY_LAT = 47
MY_LONG = -53
key = "f83bda1d52d74dba4cfb9c0e922b89f1"
url = "https://api.openweathermap.org/data/2.5/onecall"
city_name = "Amesbury"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=url, params=params)
response.raise_for_status()

data = response.json()

# for index, hour in enumerate(data['hourly']):
#     if index < 12:
#         for weather in hour['weather']:
#             if weather['id'] < 600:
#                 print("Bring an umbrella")
#             elif weather['id'] < 700:
#                 print("It's going to snow")

hourly_data = data['hourly'][:12]

# for hour in hourly_data:
#     for weather in hour['weather']:
#         if weather['id'] < 600:
#             print("Bring an umbrella")
#         elif weather['id'] < 700:
#             print("It's going to snow")

will_rain = False

for hour in hourly_data:
    for weather in hour['weather']:
        if weather['id'] < 600:
            will_rain = True

if will_rain:
    print("Bring an umbrella.")

