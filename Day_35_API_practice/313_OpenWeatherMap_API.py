import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# SECURITY: Load environment variables from .env file (NOT in version control!)
# Never commit .env to Git; add to .gitignore
load_dotenv("../.env")

# API endpoints
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# SECURITY: Retrieve sensitive credentials from environment variables
# If .env file is missing, os.getenv() returns None and code will fail
# This is intentional—forces you to set up credentials before running
api_key = os.getenv("weather_api_key")
# http://twil.io/secure - Twilio guide on securing credentials
# https://www.twilio.com/blog/environment-variables-python - General best practices

account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")

# PATTERN: API parameters passed as dict (see Day 33)
parameters = {
    "lat": 43.023979,        # Observer latitude
    "lon": -70.913673,       # Observer longitude
    "appid": api_key,        # OpenWeatherMap requires API key
}

# API: Fetch hourly weather forecast
response = requests.get(url=weather_endpoint, params=parameters)
response.raise_for_status()  # PATTERN: Check status before parsing
print(f"status code: {response.status_code}")

# PATTERN: Extract nested data from API response
# response.json() returns {"hourly": [...], "daily": [...], ...}
# ['hourly'] is list of 48 hourly forecasts
data = response.json()['hourly']

# ALGORITHM: Check next 12 hours for rain
# Weather ID < 700 indicates precipitation (rain, snow, etc.)
# Reference: https://openweathermap.org/weather-conditions
is_raining = False
for i in range(12):
    # data[i] = hour i's forecast (dict)
    # data[i]['weather'] = list of weather conditions
    # data[i]['weather'][0] = primary condition
    # data[i]['weather'][0]['id'] = numeric code
    if data[i]['weather'][0]['id'] < 700:
        is_raining = True

# PATTERN: Conditional notification (only call API if needed)
if is_raining:
    # API: Send SMS via Twilio
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                body="It's going to rain today. Bring an ☂️",
                from_='+16075245651',  # Twilio-provided virtual number
                to='+16034988677'      # Verified recipient number
            )
    # 'submitted' = successfully queued for delivery
    print(message.status)


