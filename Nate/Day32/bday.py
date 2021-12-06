##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import os

replacement_string = "[NAME]"


def send_mail(email, contents):
    print(email)
    print(contents)


def random_letter():
    templates = os.listdir('./letter_templates')
    rand_letter = random.choice(templates)
    return f'./letter_templates/{rand_letter}'


now = dt.datetime.now()
try:
    df = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    with open("birthdays.csv", 'w') as f:
        pass

for index, row in df.iterrows():
    if row['month'] == now.month and row['day'] == now.day:

        with open(random_letter(), 'r') as f:
            letter = f.read()
            letter = letter.replace(replacement_string, row['name'])
            send_mail(row['email'], letter)


