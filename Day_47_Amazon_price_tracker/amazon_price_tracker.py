import os
from bs4 import BeautifulSoup
import lxml
import smtplib
import requests
from dotenv import load_dotenv

# PATTERN: Load credentials from .env file (never hardcode passwords!)
load_dotenv("../.env")
mistwire_yahoo_account = os.getenv("mistwire_yahoo_account")
mistwire_yahoo_password = os.getenv("mistwire_yahoo_password")

# SCRAPING: Product URL to monitor
URL = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=dp_fod_1?pd_rd_i=B06Y1MP2PY&psc=1"

# PATTERN: Headers spoof browser User-Agent (Amazon blocks scrapers without browser-like headers)
# KEY CONCEPT: User-Agent identifies request source; real browser values bypass blocks
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept-Language': 'en-US,en;q=0.5'  # Accept language preference
}

# SCRAPING: Fetch page with spoofed headers
response = requests.get(URL, headers=headers)

# PATTERN: Use 'lxml' parser (faster than 'html.parser', requires: pip install lxml)
soup = BeautifulSoup(response.text, 'lxml')

# SCRAPING: Find price in <span class="a-offscreen"> tag
# Amazon uses a-offscreen for accessibility (text not visible but in HTML)
price = soup.find(name="span", class_="a-offscreen")

# LOGIC: Extract numeric price from text like "$123.45"
# .string gets text content; .split("$")[1] gets part after "$"; float converts to number
price = float(price.string.split("$")[1])
print(price)

# AUTOMATION: Send email alert if price is below threshold ($200)
if price <= 200:
    # PATTERN: SMTP context manager (with statement) ensures connection closes properly
    # SMTP port 587 is standard for encrypted email
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        # KEY CONCEPT: starttls() encrypts email connection (security best practice)
        connection.starttls()
        # AUTHENTICATION: Login with email credentials
        connection.login(user=mistwire_yahoo_account, password=mistwire_yahoo_password)
        # SENDING: Compose and send email with price alert
        # Format: "Subject: Title\n\nBody" (blank line separates subject from body)
        connection.sendmail(
            from_addr=mistwire_yahoo_account,
            to_addrs="chrisfwilliams@gmail.com",
            msg=f"Subject:Price Alert!!!\n\n"
                f"The price of the item you are monitoring is ${price}"
                f", below your purchase threshold"
        )

