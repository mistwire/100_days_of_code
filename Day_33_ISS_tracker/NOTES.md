# Day 33: ISS Tracker -- Real-Time Satellite Monitoring with APIs

## What You Learned
APIs are web interfaces that expose data and functionality. The `requests` library is used to make HTTP requests to APIs, parse responses (typically JSON), and integrate real-world data into Python programs. You built an ISS notification system combining multiple APIs and email alerts.

---

## Key Concepts

### 1. HTTP Requests & the Requests Library
The `requests` module simplifies HTTP communication by abstracting complex socket operations. Key methods:
- `requests.get()` - Retrieve data (idempotent, safe)
- `requests.post()` - Submit data (creates new resource)
- `requests.put()` - Update data (replaces entire resource)
- `requests.delete()` - Remove data

```python
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raises HTTPError for bad status codes
data = response.json()  # Parse JSON response
```

**Why**: Requests abstracts TCP sockets, headers, encoding—vastly simpler than raw networking.

### 2. JSON Parsing & Data Extraction
JSON responses are parsed into Python dictionaries using `.json()`. Nested data requires chained dictionary access:

```python
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

**Why**: APIs return structured data; parsing converts it into usable Python objects.

### 3. API Parameters
APIs accept query parameters via the `params` dictionary instead of hardcoding values in the URL:

```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,  # ISO 8601 timestamp format
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
```

**Why**: Parameters separate data (values) from logic (endpoint), making code flexible and maintainable.

### 4. API Authentication & Headers
Protected endpoints require authentication via HTTP headers:

```python
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "x-app-id": APP_ID,
}
response = requests.get(url=endpoint, headers=headers, params=query)
```

**Why**: Headers authenticate and provide metadata; `.env` files store secrets to prevent GitHub exposure.

### 5. Geolocation & Proximity Logic
Comparing coordinates to detect when the ISS is nearby:

```python
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    return True  # ISS is within 5 degrees
```

**Why**: Simplifying latitude/longitude to degree ranges avoids expensive distance calculations.

### 6. Datetime Handling & Sunset Detection
The `datetime` module works with UTC time and parsing API timestamps:

```python
import datetime as dt
time_now = dt.datetime.now(dt.timezone.utc)
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
if time_now.hour >= sunset or time_now.hour <= sunrise:
    # It's dark!
```

**Why**: ISS visibility requires darkness; UTC ensures consistency across locations.

### 7. SMTP Email Alerts
Using `smtplib` to send emails from a Gmail account:

```python
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # Upgrade to TLS encryption
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=recipient, msg=f"Subject:ISS Alert\n\nMessage body")
```

**Why**: Automated alerts keep the user informed; context manager (`with`) ensures the connection closes safely.

### 8. Looping & Polling
The main program polls APIs in an infinite loop with delays:

```python
import time
while True:
    if iss_isclose() and is_dark():
        # Send email
    time.sleep(60)  # Check every 60 seconds
```

**Why**: Polling periodically checks conditions; sleep avoids overwhelming the API or server.

---

## Common Pitfalls
- **Exposing API keys in code**: Store secrets in `.env` and use `load_dotenv()` (see Day 35).
- **Forgetting `.raise_for_status()`**: Always check response status before using `.json()`.
- **Parsing errors from empty arrays**: Use `try/except IndexError` when accessing API results.
- **Hardcoding credentials**: Email passwords and tokens should never be in source control.
- **Timezone confusion**: APIs often return UTC; be explicit about timezone conversions.
- **Not handling connection errors**: Use `try/except requests.exceptions.RequestException` for robust code.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 27 (Tkinter)** | GUI for displaying ISS position updates |
| **Day 28 (Pomodoro)** | Similar `while True` loop with `time.sleep()` for periodic tasks |
| **Day 34 (Quiz GUI API)** | Data fetched from Open Trivia API; similar parsing pattern |
| **Day 35 (Weather API)** | Uses OpenWeatherMap API; demonstrates environment variables |
| **Day 36 (Stock Tracker)** | Multiple APIs (Alpha Vantage, NewsAPI) combined in one program |
| **Day 39 (Flight Deals)** | Kiwi.com flight API; notification system with SMS/email |
| **Day 40 (Flight Club)** | Extended version with email notifications to multiple users |

---

## Before You Move On

Make sure you can:
- [ ] Make GET requests and parse JSON responses from public APIs
- [ ] Extract nested data from JSON using dictionary chaining
- [ ] Pass query parameters to API endpoints
- [ ] Authenticate to private APIs using headers and tokens
- [ ] Send emails via SMTP with `smtplib`
- [ ] Store sensitive credentials in `.env` files
- [ ] Implement polling loops with periodic checks and delays
- [ ] Handle API errors (bad status codes, missing data) gracefully
- [ ] Convert ISO 8601 timestamps to readable formats

---

## Practice Prompt
Build a **Sunrise/Sunset Notification System**: Create a program that checks the sunrise and sunset times for your location daily (using sunrise-sunset.org API) and sends you an email or SMS alert at 6 AM with today's times. Then extend it to monitor when the sun rises/sets to trigger an IoT light automation (or just log to a file as a mock).
