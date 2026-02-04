# Day 36: Stock Tracker -- Multi-API Integration & Financial Data

## What You Learned
You integrated multiple APIs (Alpha Vantage for stock prices, NewsAPI for financial news) to track stock price changes and fetch relevant news articles. You also calculated percentage changes, compared thresholds, and sent structured SMS notifications with both data and context.

---

## Key Concepts

### 1. Working with Multiple APIs in One Application
Combining data from different APIs to create more powerful features:

```python
# API 1: Alpha Vantage (stock market data)
r_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = r_stock.json()["Time Series (Daily)"]

# API 2: NewsAPI (financial news)
r_news = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = r_news.json()['articles'][:3]  # Top 3 articles
```

**Why**: No single API has everything. Combining sources gives users complete context (price + news).

### 2. Converting Dictionaries to Lists
Extracting values from a dictionary to work with them as a list:

```python
# stock_data is a dict where keys are dates, values are OHLC data
# {"2024-02-04": {...}, "2024-02-03": {...}, ...}

# Convert dict items to list for indexed access
daily_values = [value for (key, value) in stock_data.items()]

# Now access by index: [0] = today, [1] = yesterday, etc.
yesterdays_close = float(daily_values[0]['4. close'])
day_before_close = float(daily_values[1]['4. close'])
```

**Why**: Working with indices is faster than iterating dict keys repeatedly.

### 3. Percentage Change Calculation
Computing percent change between two values (common in finance):

```python
def get_change(current, previous):
    if current == previous:
        return 100.0  # Avoid showing 0% for no change
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

percent_change = round(get_change(yesterdays_close, day_before_close))
```

**Formula**: `|current - previous| / previous * 100`

**Why**: Percentage changes are more meaningful than absolute changes (a $10 change is huge for a $20 stock, negligible for a $1000 stock).

### 4. Threshold-Based Alerts
Only send notifications when a condition is met:

```python
ALERT_THRESHOLD = 5  # Alert if price changes >= 5%

if abs(percent_change) >= ALERT_THRESHOLD:
    # Fetch news and send alert
    r_news = requests.get(NEWS_ENDPOINT, params=news_params)
    # Send SMS
else:
    # Don't notify (reduces API calls and SMS costs)
    pass
```

**Why**: Reduces noise (don't alert for minor fluctuations) and saves costs (SMS charges accumulate).

### 5. Emoji & Unicode in SMS
Including symbols in text messages for better readability:

```python
up_down = None
if difference > 0:
    up_down = "⬆️"  # Up arrow emoji
else:
    up_down = "⬇️"  # Down arrow emoji

message = f"{STOCK_NAME}: {up_down} {percent_change}%"
```

**Why**: Emojis add visual clarity; recipients immediately see trend without reading.

### 6. Looping Over API Results
Iterating arrays from API responses:

```python
news_data = r_news.json()['articles'][:3]  # Slice to first 3
for i in range(len(news_data)):
    headline = news_data[i]['title']
    brief = news_data[i]['description']
    # Send SMS with this article
```

**Why**: APIs return arrays; you need to loop to extract and use individual items.

### 7. Building Structured Notification Messages
Formatting data into readable, scannable text:

```python
message = client.messages.create(
    body=f"{STOCK_NAME}: {up_down} {percent_change}%\n"
         f"Headline: {headline}\n"
         f"Brief: {brief}",
    from_=TWILIO_PHONE,
    to=MY_PHONE
)
```

**Why**: Clear formatting helps recipients understand data at a glance; newlines separate concerns.

### 8. Error Handling in Financial Code
Gracefully handling edge cases:

```python
def get_change(current, previous):
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0  # Previous price was 0 (stock delisted or new)
```

**Why**: Real data is messy; previous price might be 0 if stock is new or problematic.

---

## Common Pitfalls
- **Not slicing API results**: NewsAPI returns many articles; use `[:3]` to get just the most relevant.
- **Hardcoding thresholds**: Use constants (`ALERT_THRESHOLD = 5`) so you can change them easily.
- **Forgetting to convert strings to floats**: API data comes as strings; convert before math.
- **Dividing by zero**: Stock delisted? Previous price is 0. Always check before dividing.
- **Sending too many SMS**: Each SMS costs money. Only notify when threshold is met.
- **Not reading API docs**: Alpha Vantage has rate limits (5 calls/min free tier); NewsAPI has daily limits.
- **Concatenating floats without formatting**: Shows "4.152000000000001%"; use `round()` or format strings.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 35 (Weather API)** | Environment variables for API keys; multiple APIs in one program |
| **Day 33 (ISS Tracker)** | Looping, API fetching, conditional logic |
| **Day 34 (Quiz API)** | Parsing API responses and extracting nested data |
| **Day 37 (Habit Tracker)** | HTTP POST requests; headers and authentication |
| **Day 38 (Workout Tracker)** | Multiple APIs (Nutritionix, Sheety); parsing responses |
| **Day 39-40 (Flight Deals)** | Multi-API integration; threshold alerts; notifications |

---

## Before You Move On

Make sure you can:
- [ ] Fetch data from Alpha Vantage (stock prices) and NewsAPI (articles)
- [ ] Convert dictionary to list and access by index
- [ ] Calculate percentage change between two values
- [ ] Use conditional logic to alert only when threshold is met
- [ ] Extract and loop over API results (headlines, descriptions)
- [ ] Format structured messages with multiple data points
- [ ] Handle edge cases (zero previous price, missing data)
- [ ] Build and send SMS messages with multiple lines of data
- [ ] Understand API rate limits and respect them

---

## Practice Prompt
Build a **Multi-Stock Portfolio Tracker**: Create a program that:
1. Reads a list of stock symbols from a CSV file (e.g., `portfolio.csv` with columns: symbol, shares, purchase_price)
2. Fetches current prices for each stock via Alpha Vantage
3. Calculates gain/loss and percentage return for each position
4. Ranks stocks by performance (best to worst)
5. Sends a daily summary SMS/email showing:
   - Total portfolio value
   - Gains/losses ($ and %)
   - Top 3 best/worst performers
   - Alerts if any stock drops > 10%

Bonus: Display a formatted table in the console; use Google Sheets API to log historical data.
