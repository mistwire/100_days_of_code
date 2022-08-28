import os
from bs4 import BeautifulSoup
import lxml
import smtplib
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
mistwire_yahoo_account = os.getenv("mistwire_yahoo_account")
mistwire_yahoo_password = os.getenv("mistwire_yahoo_password")


URL = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=dp_fod_1?pd_rd_i=B06Y1MP2PY&psc=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept-Language': 'en-US,en;q=0.5'
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

price = soup.find(name="span", class_="a-offscreen")
price = float(price.string.split("$")[1])
print(price)


if price <= 200:
    with smtplib.SMTP ("smtp.mail.yahoo.com", port=587) as connection:
        # start and secure connection to email server:
        connection.starttls()
        # login
        connection.login(user=mistwire_yahoo_account, password=mistwire_yahoo_password)
        # send!
        connection.sendmail(
            from_addr=mistwire_yahoo_account,
            to_addrs="chrisfwilliams@gmail.com",
            msg=f"Subject:Price Alert!!!\n\nThe price of the item you are monitoring is ${price}"
                f", below your purchase threshold")

