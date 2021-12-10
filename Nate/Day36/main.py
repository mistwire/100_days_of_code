import datetime as dt
from datetime import date
import requests
from twilio.rest import Client
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_api_key = "9AJX6HRVW9KOJK63"
alpha_uri = "https://www.alphavantage.co/query"
alpha_function = "TIME_SERIES_DAILY"
stock_sym = "NIO"

TWILIO_ACCOUNT_SID = "AC9f71e683a403031c1c5a6dc4ec10959a"
TWILIO_NUMBER = "+15304831979"
MY_NUMBER = "+13039173568"

newsapi_key = "624823829e3346a788845a6d849920a6"
news_uri = "https://newsapi.org/v2/everything"


def get_news(query):
    import requests

    params = {
            'q': query,
            'from': day_before,
            'to': yesterday,
            'apiKey': newsapi_key
       }

    r = requests.get(url=news_uri, params=params)

    return r.json()


def send_twilio_msg(message):
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(TWILIO_ACCOUNT_SID, auth_token)

    message = client.messages \
                    .create(
                         body=message,
                         from_=TWILIO_NUMBER,
                         to=MY_NUMBER
                     )

    print(message.sid)


yesterday = str(date.today() - dt.timedelta(days=1))
day_before = str(date.today() - dt.timedelta(days=2))

alpha_params = {
    "function": alpha_function,
    "symbol": stock_sym,
    "apikey": alpha_api_key
}

response = requests.get(url=alpha_uri, params=alpha_params)
response.raise_for_status()

data = response.json()

yesterday_close = float(data['Time Series (Daily)'][yesterday]['4. close'])
day_before_close = float(data['Time Series (Daily)'][day_before]['4. close'])

delta_price = round((day_before_close - yesterday_close), 2)

percent_change = round(((delta_price / day_before_close) * 100), 2)

change = abs(percent_change)

if change > 2:
    news = get_news("Tesla")
    articles = news['articles'][:3]
    message = ""
    if percent_change < 0:
        message += f"TSLA: 🔻{percent_change}%\n"
        print(f"{stock_sym} went down by {change}%")
    elif percent_change > 0:
        message += f"TSLA: 🔺{percent_change}%\n"
        print(f"{stock_sym} went up by {change}%")
    else:
        print(f"{stock_sym} had no change")

    for article in articles:
        headline = article['title']
        brief = article['description']
        message += f"Headline: {headline}\n"
        message += f"Brief: {brief}\n\n"

    send_twilio_msg(message)


