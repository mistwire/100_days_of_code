# Day 35: Weather API -- Environment Variables & API Key Security

## What You Learned
You learned how to securely manage API keys and sensitive credentials using environment variables and the `python-dotenv` library. This is critical for any production code that interacts with APIs. You also integrated the OpenWeatherMap API with Twilio SMS notifications to build a practical weather alert system.

---

## Key Concepts

### 1. Environment Variables & `.env` Files
Sensitive data (API keys, passwords, tokens) should NEVER be hardcoded or committed to version control:

```python
# BAD - Never do this!
api_key = "abc123xyz789"  # Exposed if code is public

# GOOD - Use environment variables
import os
from dotenv import load_dotenv

load_dotenv("../.env")  # Load .env file from parent directory
api_key = os.getenv("weather_api_key")  # Retrieve from environment
```

`.env` file (in parent directory, NOT in version control):
```
weather_api_key=abc123xyz789
twilio_account_sid=ACxxxxxx
twilio_auth_token=auth_token_here
```

Add `.env` to `.gitignore`:
```
.env
.env.local
*.pem
secrets/
```

**Why**: If your repo is public, anyone can steal your API keys and use them maliciously (costing you money, accessing your data, etc.).

### 2. Multiple API Integration
Combining data from different APIs to create more powerful applications:

```python
# Fetch weather data from OpenWeatherMap
response = requests.get(url=weather_endpoint, params=parameters)
weather_data = response.json()['hourly']

# Check if it will rain
is_raining = False
for i in range(12):
    if weather_data[i]['weather'][0]['id'] < 700:  # < 700 = precipitation
        is_raining = True

# If yes, send SMS via Twilio
if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an ☂️",
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
```

**Why**: Single APIs often lack features; combining them creates comprehensive solutions.

### 3. Weather Code Interpretation
OpenWeatherMap uses numeric codes for weather conditions:

```python
# Weather code < 700 indicates precipitation (rain, snow, etc.)
# 200-299: Thunderstorm
# 300-399: Drizzle
# 500-599: Rain
# 600-699: Snow
# 700+: Mist, smoke, haze, dust, fog, sand, ash

if data[i]['weather'][0]['id'] < 700:
    is_raining = True
```

**Why**: API responses use codes for efficiency; you need documentation to interpret them.

### 4. ISO 8601 Time Format
APIs often return timestamps in ISO 8601 format (YYYY-MM-DDTHH:MM:SS):

```python
import datetime

# Parse ISO timestamp
timestamp = "2024-02-04T12:30:45Z"
# Extract hour: split on "T", then take first part of HH:MM:SS
hour = int(timestamp.split("T")[1].split(":")[0])

# Or use datetime parsing
from datetime import datetime
dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
hour = dt.hour
```

**Why**: ISO format is unambiguous and timezone-aware; splitting is quick but fragile.

### 5. API Response Nesting & Array Iteration
Real APIs return complex nested data; navigating it requires understanding the structure:

```python
data = response.json()['hourly']  # Extract 'hourly' array
for i in range(12):
    weather_id = data[i]['weather'][0]['id']
    # data[i] = hour i's data (dict)
    # data[i]['weather'] = array of weather conditions
    # data[i]['weather'][0] = first (main) weather condition
    # data[i]['weather'][0]['id'] = numeric code
```

**Why**: APIs nest data hierarchically; you must know the schema to extract what you need.

### 6. SMS Notifications with Twilio
Twilio provides a simple API for sending SMS messages:

```python
from twilio.rest import Client

account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Weather alert: Rain expected!",
    from_=TWILIO_VIRTUAL_NUMBER,  # Twilio-provided number
    to=MY_PHONE_NUMBER             # Your verified phone
)
print(message.sid)  # Unique message ID
```

**Why**: Twilio abstracts SMS protocol complexity; sending is just a few lines.

### 7. Conditional Logic Based on Data
Real-world programs make decisions based on API data:

```python
if is_raining:
    # Send notification
    client.messages.create(...)
else:
    # Don't send (save API quota)
    print("No rain expected")
```

**Why**: APIs cost money; only call expensive operations when necessary.

---

## Common Pitfalls
- **Committing `.env` files to Git**: Use `.gitignore` to exclude them.
- **Not handling missing environment variables**: `os.getenv("KEY")` returns `None` if not found; use `os.getenv("KEY", "default")` for defaults or raise an error.
- **Hardcoding paths to `.env`**: Use relative paths or check multiple locations.
- **Ignoring API documentation**: Different APIs have different response structures; always read the docs.
- **Not rate-limiting API calls**: Free tiers have limits; sleep between requests or check remaining quota.
- **Extracting wrong array indices**: `weather[0]` is the main condition; `weather[1]` might not exist.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 28 (Pomodoro)** | Similar `.env` usage for sensitive data |
| **Day 33 (ISS Tracker)** | API fetching; hardcoded credentials (WRONG!) vs. environment variables (CORRECT!) |
| **Day 34 (Quiz API)** | Parsing API responses; this shows secure approach |
| **Day 36 (Stock Tracker)** | Multiple APIs (Alpha Vantage, NewsAPI); environment variable pattern |
| **Day 37 (Habit Tracker)** | Pixe.la API with authentication headers |
| **Day 38 (Workout Tracker)** | Nutritionix API; Sheety API; multiple endpoints |
| **Day 39-40 (Flight Deals)** | Kiwi.com flight API; Sheety; notification manager |

---

## Before You Move On

Make sure you can:
- [ ] Create and use a `.env` file with `load_dotenv()` and `os.getenv()`
- [ ] Add `.env` to `.gitignore` to prevent accidental commits
- [ ] Fetch data from OpenWeatherMap API using latitude/longitude
- [ ] Parse nested JSON arrays and access deep properties
- [ ] Interpret weather codes (< 700 = rain)
- [ ] Parse ISO 8601 timestamps and extract hours
- [ ] Send SMS via Twilio using account SID and auth token
- [ ] Make conditional decisions based on API data
- [ ] Handle API errors gracefully (missing data, rate limits)

---

## Practice Prompt
Build a **Daily Weather Summary Email**: Create a program that fetches the forecast for the next 7 days and sends you a daily email at 6 AM with:
- High/low temperature
- Chance of precipitation
- UV index (if available)
- Recommended activities (e.g., "Great day for hiking!" if sunny)

Use OpenWeatherMap (free tier allows many calls) and schedule it to run via cron or task scheduler. Bonus: Add a feature to notify multiple users by storing emails in a CSV and looping through them.
