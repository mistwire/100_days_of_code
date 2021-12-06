import datetime as dt
import random

now = dt.datetime.now()
date_of_birth = dt.datetime(year=1980, month=1, day=22)


def send_email(contents):
    # don't feel like setting up an email account....
    print(contents)


quote_list = []
if now.weekday() == 6:
    with open("quotes.txt", 'r') as f:
        quote_list = f.readlines()

    random_quote = random.choice(quote_list)

    send_email(random_quote)


