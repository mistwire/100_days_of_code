import smtplib
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("../.env")
TWILIO_SID = os.getenv("twilio_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("twilio_auth_token")
TWILIO_VIRTUAL_NUMBER = '+16075245651'
TWILIO_VERIFIED_NUMBER = '+16034988677'

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "mistwire.test01@gmail.com"
MY_PASSWORD = "Severe-Merchant-Peace-10"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )