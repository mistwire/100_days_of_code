# API: sunrise-sunset.org provides sunrise/sunset times by latitude/longitude
# https://www.w3schools.com/python/ref_string_split.asp
# https://sunrise-sunset.org/api

import requests
import datetime as dt

MY_LAT = 43.0203247
MY_LONG = -70.931396

# KEY CONCEPT: API parameters separate data (values) from endpoint (logic)
# Sunset API requires location via query parameters instead of URL path
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,  # Return ISO 8601 timestamps (e.g., "2024-02-04T12:30:45+00:00")
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']
# print(sunrise)
# PATTERN: Parse ISO 8601 timestamp to extract hour
# Format: "2024-02-04T12:30:45+00:00" -> split("T")[1] -> "12:30:45+00:00" -> split(":")[0] -> "12"
# print(sunrise.split("T")[1].split(":")[0])
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)  # Hour as string (e.g., "07")
print(sunset)   # Hour as string (e.g., "17")

# KEY CONCEPT: Use UTC time to avoid timezone conversion bugs
# ISS position data is in UTC; comparing with local time would be incorrect
time_now = dt.datetime.now(dt.timezone.utc)

print(time_now.hour)  # Current UTC hour (0-23)

