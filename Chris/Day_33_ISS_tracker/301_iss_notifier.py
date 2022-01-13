import math

import requests
import datetime as dt


def iss_isclose(iss_lat, iss_long):
    if math.isclose(iss_lat, MY_LAT, abs_tol=5) and math.isclose(iss_long, MY_LONG, abs_tol=5):
        return True
    else:
        return False


def is_dark():
    if sunrise >= time_now.hour <= sunset:
        print("it's dark!")


MY_LAT = 43.0203247 # Your latitude
MY_LONG = -70.931396 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude)
print(iss_longitude)

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"sunrise {sunrise}")
print(f"sunset {sunset}")

time_now = dt.datetime.now(dt.timezone.utc)
print(f"time now {time_now}")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(iss_isclose(iss_latitude, iss_longitude))

is_dark()

