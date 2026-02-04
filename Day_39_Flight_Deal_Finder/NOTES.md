# Day 39: Flight Deal Finder -- Web Scraping-Like Data Management with APIs

## What You Learned
You built a flight deal finder that monitors prices across multiple destinations and alerts users via SMS when prices drop below a threshold. This project integrated three APIs (Kiwi.com for flights, Sheety for data storage, Twilio for notifications) and introduced data management patterns crucial for production applications.

---

## Key Concepts

### 1. Multi-Class Architecture for Complex Projects
Breaking a project into logical, reusable classes:

```python
# main.py: Orchestrator
data_manager = DataManager()          # Manages Google Sheet data
flight_search = FlightSearch()        # Searches flights via Kiwi.com API
notification_manager = NotificationManager()  # Sends SMS alerts

# Each class has single responsibility:
# - DataManager: Data persistence (Google Sheets via Sheety API)
# - FlightSearch: Flight data (Kiwi.com API)
# - NotificationManager: Notifications (Twilio SMS)
```

**Why**: Separation of concerns makes code testable, maintainable, and reusable. Each class does one thing well.

### 2. Initializing Databases & Checking Completeness
Populating missing data on first run:

```python
sheet_data = data_manager.get_destination_data()

# If IATA codes are empty, populate them
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
```

**Why**: Google Sheet columns might not have all required data initially. Auto-populate on first run improves UX.

### 3. Converting City Names to IATA Codes
Kiwi.com flights require airport codes (BOS, JFK, DEN), not city names:

```python
def get_destination_code(self, city_name):
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    query = {
        "term": city_name,              # "Boston"
        "location_types": "city"
    }
    r = requests.get(url=location_endpoint, headers=headers, params=query)
    results = r.json()["locations"]
    code = results[0]['code']           # "BOS"
    return code
```

**Why**: Users know city names; APIs need standardized codes. The API translates between them.

### 4. Date Range Queries
Searching flights within a date range:

```python
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
```

**Why**: Users want to plan ahead. Searching 6-month window finds best deals across many departure dates.

### 5. Formatting Dates for API Queries
Converting Python datetime to API-required format:

```python
from_time.strftime("%d/%m/%Y")  # "05/02/2024"
to_time.strftime("%d/%m/%Y")    # "06/30/2024"

# Build API query with formatted dates
query = {
    "fly_from": origin_city_code,
    "fly_to": destination_city_code,
    "date_from": from_time.strftime("%d/%m/%Y"),
    "date_to": to_time.strftime("%d/%m/%Y"),
    ...
}
```

**Why**: APIs have specific format requirements. Kiwi.com uses DD/MM/YYYY (European format).

### 6. Extracting Flight Details from Nested Responses
Real flight data is deeply nested; careful navigation is required:

```python
data = response.json()["data"][0]  # First flight result
flight_data = FlightData(
    price=data["price"],
    origin_city=data["route"][0]["cityFrom"],
    origin_airport=data["route"][0]["flyFrom"],
    destination_city=data["route"][0]["cityTo"],
    destination_airport=data["route"][0]["flyTo"],
    out_date=data["route"][0]["local_departure"].split("T")[0],
    return_date=data["route"][1]["local_departure"].split("T")[0]
)
```

**Why**: Flight routes have multiple segments (legs); you must access the right one ([0], [1], etc.).

### 7. Comparing Data & Triggering Alerts
Conditional logic based on price comparison:

```python
if flight.price < destination["lowestPrice"]:
    # Price dropped below previous low
    notification_manager.send_sms(
        message=f"Low price alert! Only ${flight.price}..."
    )
```

**Why**: Only alert when there's a deal (price < threshold). Reduces notification fatigue.

### 8. Encapsulating Configuration
Using constants for configuration instead of magic numbers:

```python
ORIGIN_CITY_IATA = "BOS"          # Boston Logan International

# Inside FlightSearch class:
query = {
    "nights_in_dst_from": 7,       # Minimum stay at destination
    "nights_in_dst_to": 28,        # Maximum stay at destination
    "flight_type": "round",        # Round-trip flights only
    "one_for_city": 1,             # One result per city
    "max_stopovers": 0,            # Direct flights only
    "curr": "USD"                  # Currency
}
```

**Why**: Configuration constants are easier to change than magic numbers. Comments explain intent.

### 9. Error Handling for Missing Data
Gracefully handling cases where no flights are found:

```python
try:
    data = response.json()["data"][0]
except IndexError:
    print(f"No flights found for {destination_city_code}.")
    return None
```

**Why**: Some routes have no available flights. Return None instead of crashing.

### 10. Data Persistence Layer
Separating API calls from data management:

```python
class DataManager:
    def get_destination_data(self):
        """Fetch destinations from Google Sheet."""
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update Google Sheet with IATA codes."""
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers,
            )
```

**Why**: Separating persistence logic makes it easy to switch from Google Sheets to database without affecting search logic.

---

## Common Pitfalls
- **Not handling IndexError when no flights found**: Always wrap `data[0]` in try/except.
- **Forgetting to check IATA code population**: If codes are empty, searches fail silently.
- **Using wrong date format**: Kiwi.com uses DD/MM/YYYY (European), not MM/DD/YYYY (American).
- **Not updating Google Sheet with codes**: Once populated, code should update the sheet so you don't re-fetch next run.
- **Hardcoding destination list**: Use Google Sheets so users can add/remove destinations without code changes.
- **Sending too many SMS**: Each SMS costs money. Only send when price drops below threshold.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 25 (CSV/Pandas)** | Data management (reading from CSV instead of Google Sheet) |
| **Day 35 (Weather API)** | Environment variables for API keys |
| **Day 36 (Stock Tracker)** | Threshold-based alerts and multi-API integration |
| **Day 37 (Habit Tracker)** | Google Sheets via Sheety API; PUT requests |
| **Day 38 (Workout Tracker)** | Multi-API integration and data transformation |
| **Day 40 (Flight Club)** | Extended version with email notifications and stopovers |

---

## Before You Move On

Make sure you can:
- [ ] Design classes with single responsibilities (SRP)
- [ ] Fetch data from Google Sheets via Sheety API
- [ ] Update Google Sheets rows via PUT requests
- [ ] Convert city names to IATA codes via location API
- [ ] Query flight APIs with date ranges and parameters
- [ ] Extract nested data from flight responses (route[0], route[1], etc.)
- [ ] Handle missing data gracefully (IndexError for no flights)
- [ ] Compare prices and trigger alerts based on thresholds
- [ ] Send SMS notifications via Twilio with formatted messages
- [ ] Orchestrate multiple classes/APIs in main.py

---

## Practice Prompt
Build a **Hotel & Flight Deal Finder**: Extend this project to:
1. Track hotel prices in addition to flights (use booking.com or similar API)
2. Match flights with hotels:
   - If cheap flight to Barcelona AND cheap hotel in Barcelona → Alert
   - Combine costs to show total trip price
3. Track price history (store daily prices in separate Google Sheet)
4. Display trends:
   - "Prices are rising! Last chance to book at $XXX"
   - "Best price in 30 days was $XXX on {date}"
5. Allow users to set flexible departure dates:
   - "Show me any deal to Europe ±2 weeks from my preferred date"

Bonus: Integrate with Google Calendar API to avoid suggesting trips during user's busy periods.
