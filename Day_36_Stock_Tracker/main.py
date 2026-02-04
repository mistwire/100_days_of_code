import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Configuration
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# SECURITY: Load credentials from .env file
load_dotenv("../.env")
stock_apikey = os.getenv("stock_apikey")
news_apikey = os.getenv("news_apikey")
twilio_account_sid = os.getenv("twilio_account_sid")
twilio_auth_token = os.getenv("twilio_auth_token")

# API 1: Alpha Vantage (stock market data)
# https://www.alphavantage.co/documentation/
stock_params = {
    "function": "TIME_SERIES_DAILY",  # Daily closing prices
    "symbol": STOCK_NAME,
    "apikey": stock_apikey
}

# API 2: NewsAPI (financial news)
# https://newsapi.org/docs
news_params = {
    "qInTitle": COMPANY_NAME,  # Search for articles with company name in title
    "language": "en",
    "apiKey": news_apikey,
}

# Fetch stock data
r_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = r_stock.json()["Time Series (Daily)"]

# PATTERN: Convert dict to list to access by index
# stock_data = {"2024-02-04": {...}, "2024-02-03": {...}, ...}
# daily_values = [{...}, {...}, ...] (list of dicts)
# daily_values[0] = today's data, daily_values[1] = yesterday's data
daily_values = [value for (key, value) in stock_data.items()]

# PATTERN: Extract closing prices and convert to float for math
yesterdays_close = float(daily_values[0]['4. close'])      # Today (most recent)
day_before_close = float(daily_values[1]['4. close'])      # Yesterday

# Calculate absolute price change
difference = abs(yesterdays_close - day_before_close)

# PATTERN: Determine direction (up/down) based on comparison
up_down = None
if difference > 0:
    up_down = "⬆️"  # Emoji for up (more visually clear than "UP")
else:
    up_down = "⬇️"  # Emoji for down


def get_change(current, previous):
    """Calculate percentage change between two values.

    Args:
        current: Current price
        previous: Previous price

    Returns:
        float: Percentage change (always positive, use up_down variable for direction)
    """
    if current == previous:
        return 100.0  # Arbitrary non-zero value for no change
    try:
        # ALGORITHM: (|current - previous| / previous) * 100
        # e.g., (200 - 100) / 100 * 100 = 100% gain
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0  # Previous price was 0 (stock delisted, problematic data)


# Calculate percent change
percent_change = round(get_change(yesterdays_close, day_before_close))

# PATTERN: Threshold-based alert (only notify if significant change)
# Alert threshold = 5% (arbitrary; could be configurable)
# This prevents notifications for minor price movements and saves API/SMS costs
if abs(percent_change) >= 5:
    # Fetch news articles about this stock
    r_news = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = r_news.json()['articles'][:3]  # Slice to first 3 articles

    # PATTERN: Loop over results and send one SMS per article
    # (Each SMS costs money, but provides context for the price move)
    for i in range(len(news_data)):
        headline = news_data[i]['title']
        brief = news_data[i]['description']

        # Send SMS via Twilio
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            # PATTERN: Format message with multiple data points separated by newlines
            body=f"{STOCK_NAME}: {up_down} {percent_change}%\n"
                 f"Headline: {headline}\n"
                 f"Brief: {brief}",
            from_='+16075245651',
            to='+16034988677'
        )

