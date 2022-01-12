# https://www.w3schools.com/python/ref_string_split.asp
# https://sunrise-sunset.org/api
#

import requests
import datetime as dt

MY_LAT = 43.0203247
MY_LONG = -70.931396

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']
# print(sunrise)
# print(sunrise.split("T")[1].split(":")[0])
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = dt.datetime.now(dt.timezone.utc)

print(time_now.hour)

