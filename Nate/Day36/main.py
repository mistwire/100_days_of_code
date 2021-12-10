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


def get_news():
    import requests

    params = {
            'q': stock_sym,
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

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

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

if change > 5:
    news = get_news()
    print(news)
    if percent_change < 0:
        print(f"{stock_sym} went down by {change}%")
    elif percent_change > 0:
        print(f"{stock_sym} went up by {change}%")
    else:
        print(f"{stock_sym} had no change")

