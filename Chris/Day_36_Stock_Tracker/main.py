import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv(".env")
stock_apikey = os.getenv("stock_apikey")
news_apikey = os.getenv("news_apikey")
twilio_account_sid = os.getenv("twilio_account_sid")
twilio_auth_token = os.getenv("twilio_auth_token")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_apikey
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "language": "en",
    "apiKey": news_apikey,
}

r_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = r_stock.json()["Time Series (Daily)"]
# convert dict to list via list comprehension & capture the values:
daily_values = [value for (key, value) in stock_data.items()]
yesterdays_close = float(daily_values[0]['4. close'])
day_before_close = float(daily_values[1]['4. close'])
difference = abs(yesterdays_close - day_before_close)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0


percent_change = round(get_change(yesterdays_close, day_before_close))
if abs(percent_change) >= 5:
    r_news = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = r_news.json()['articles'][:3]
    for i in range(len(news_data)):
        headline = news_data[i]['title']
        brief = news_data[i]['description']
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            body=f"{STOCK_NAME}: {up_down} {percent_change}%\nHeadline: {headline} \nBrief: {brief}",
            from_='+16075245651',
            to='+16034988677'
        )

