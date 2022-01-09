import datetime as dt
import random
import smtplib

my_email = "mistwire.test01@gmail.com"
password = "notreallymypassword"

# use datetime to get current day of week
now = dt.datetime.now()
day_of_week = now.isoweekday()
print(day_of_week)

# open quotes.txt and get list of quotes
with open("quotes.txt") as f:
    quotes = f.read().splitlines()

# use random to pick one quote from list
quote = random.choice(quotes)
print(quote)

# use smtplib to send me that quote if it is Saturday:
if day_of_week == 6:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # start and secure connection to email server:
        connection.starttls()
        # login
        connection.login(user=my_email, password=password)
        # send!
        connection.sendmail(
            from_addr=my_email,
            to_addrs="lupusthemonk@yahoo.com",
            msg=f"Subject:Saturday Motivation\n\n{quote}")

