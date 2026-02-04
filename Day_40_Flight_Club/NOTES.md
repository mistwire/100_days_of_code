# Day 40: Flight Club -- Advanced Features & Production Patterns

## What You Learned
You extended the flight deal finder with production-grade features: email notifications to multiple users, handling stopovers/layovers, generating Google Flights links, and using dictionary comprehensions for data aggregation. This demonstrates how to scale a prototype into a more robust, feature-rich application.

---

## Key Concepts

### 1. Dictionary Comprehensions for Data Aggregation
Converting a list of dictionaries into a lookup dictionary:

```python
# Original list from Google Sheet:
sheet_data = [
    {"iataCode": "DEN", "city": "Denver", "lowestPrice": 150, "id": 2},
    {"iataCode": "LAX", "city": "Los Angeles", "lowestPrice": 200, "id": 3},
]

# Dictionary comprehension - creates lookup by IATA code:
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

# Result:
# {
#     "DEN": {"id": 2, "city": "Denver", "price": 150},
#     "LAX": {"id": 3, "city": "Los Angeles", "price": 200},
# }

# Now look up by code: destinations["DEN"]["price"]
```

**Why**: Dictionary lookups (O(1)) are faster than searching lists (O(n)). Cleaner code for frequent lookups.

### 2. Handling Stopovers (Flights with Layovers)
Managing flights that have layovers/stops:

```python
# When direct flights (max_stopovers: 0) return no results,
# retry with stopovers allowed (max_stopovers: 1)

try:
    data = response.json()["data"][0]
except IndexError:
    # No direct flights found, try with stopovers
    query["max_stopovers"] = 1
    response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=query)
    data = response.json()["data"][0]

    # With stopovers, route has 3+ legs: [outbound, stopover, return]
    flight_data = FlightData(
        ...,
        stop_overs=1,
        via_city=data["route"][0]["cityTo"]  # City where stopover occurs
    )
```

**Why**: Sometimes cheapest option includes layovers. Giving users a choice increases deal availability.

### 3. Conditional Message Formatting
Building messages based on flight characteristics:

```python
message = f"Low price alert! Only £{flight.price}..."

if flight.stop_overs > 0:
    message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

# Message is customized based on flight type
```

**Why**: Users should know about stopovers upfront. Conditional formatting adds relevant details.

### 4. Generating Google Flights Links
Creating shareable flight booking links:

```python
link = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

# Example:
# https://www.google.com/flights?hl=en#flt=BOS.DEN.2024-02-05*DEN.BOS.2024-03-04
```

**Why**: Users can click the link to book immediately on Google Flights. Reduces friction.

### 5. Bulk Email Notifications
Sending individual emails to multiple recipients:

```python
users = data_manager.get_customer_emails()  # Fetch from Google Sheet
emails = [row["email"] for row in users]
names = [row["firstName"] for row in users]

notification_manager.send_emails(emails, message, link)

# Inside NotificationManager:
def send_emails(self, emails, message, google_flight_link):
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for email in emails:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}"
            )
```

**Why**: Notifying multiple users from a single script enables sharing deals with friends/family without manual forwarding.

### 6. Fetching Data from Multiple Google Sheets
Accessing different sheets for different purposes:

```python
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/.../flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/.../users/sheet1"

# Get destinations
destinations = data_manager.get_destination_data()

# Get subscribers
users = data_manager.get_customer_emails()
```

**Why**: Separating data (destinations vs. subscribers) into different sheets makes it easier to manage. Users can edit subscriber list without touching price data.

### 7. Skip and Continue Logic
Gracefully handling missing or invalid data:

```python
for destination_code in destinations:
    flight = flight_search.check_flights(...)

    if flight is None:
        # No flights found for this route
        continue  # Skip to next destination

    if flight.price < destinations[destination_code]["price"]:
        # Send alert
        ...
```

**Why**: Not all routes have flights. Continuing instead of crashing allows the program to check all routes.

### 8. Using SMTP Context Manager for Email
Proper resource management when sending emails:

```python
# BAD: Connection might stay open if error occurs
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.sendmail(...)
# connection.close()  # Might not execute if exception before this line

# GOOD: Context manager guarantees cleanup
with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
    connection.starttls()
    connection.sendmail(...)
    # Connection automatically closes, even if exception
```

**Why**: `with` statement ensures resources are cleaned up reliably. Important for file/network operations.

### 9. Email Message Formatting with Headers
Proper email structure with subject lines:

```python
msg = f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')

connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=email,
    msg=msg
)
```

**Why**: Email format requires "Subject:..." header. Encoding ensures special characters (emojis, accents) display correctly.

### 10. Scaling Patterns
This project demonstrates key patterns for scaling applications:

```
Local Script (Day 39)
  ↓
  + Google Sheets for data (replaces CSV)
  ↓
Production System (Day 40)
  + Multiple users
  + Advanced features (stopovers, booking links)
  + Robust error handling
  + Bulk notifications
```

**Why**: Understanding these patterns helps you scale from prototypes to production systems without major rewrites.

---

## Common Pitfalls
- **Not handling None flights**: `check_flights()` returns None when no flights found; always check before using.
- **Hardcoding user emails**: Fetch from Google Sheet so users don't need code changes to join.
- **Forgetting to encode email messages**: UTF-8 encoding prevents character corruption.
- **Not generating booking links**: Users might forget flight details; links enable immediate booking.
- **Reusing same route list**: Each stopover check should reset query parameters before retrying.
- **Not checking if stopovers are available**: Some routes genuinely have no flights; None check prevents crashes.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 20 (Snake Game)** | Similar skip/continue logic for game states |
| **Day 25 (CSV/Pandas)** | Data aggregation; this uses Google Sheets instead |
| **Day 28 (Pomodoro)** | GUI features; this uses CLI but similar architecture |
| **Day 39 (Flight Deal Finder)** | Base project; this adds advanced features |

---

## Before You Move On

Make sure you can:
- [ ] Use dictionary comprehensions to create lookup dictionaries
- [ ] Handle API fallbacks (try direct flights, retry with stopovers)
- [ ] Generate URLs with formatted parameters
- [ ] Send bulk emails to multiple recipients
- [ ] Fetch data from multiple Google Sheets via Sheety API
- [ ] Use skip/continue logic to handle missing data
- [ ] Format SMTP email messages with proper headers and encoding
- [ ] Use context managers (`with` statement) for resource management
- [ ] Build production-quality applications from prototypes

---

## Practice Prompt
Build a **Travel Group Expense Tracker**: Extend this project to:
1. Track group expenses:
   - User A books flight for group → logs expense in Sheety
   - Items: flight price, per-person share, who paid
2. Calculate balances:
   - "Person A paid £500, owes 50% (£250)"
   - "Person B paid nothing, owes £300"
   - Generate settlement plan: "B pays A £50, C pays B £100"
3. Send notifications:
   - When flight deal found → Email group with link
   - Monthly settlement report → Email who owes whom
4. Track historical flights:
   - Store booked flights in separate sheet
   - Show group's trip history

Bonus: Integrate with Stripe API to collect money from the group for shared expenses; send booking confirmation emails with flight details and hotel reservations.
