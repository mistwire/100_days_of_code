from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = ""
TWILIO_NUMBER = ""
MY_NUMBER = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client - Client(TWILIO_ACCOUNT_SID, auth_token)

    def send_twilio_msg(self, message):
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(TWILIO_ACCOUNT_SID, auth_token)

        message = client.messages \
            .create(
             body=message,
             from_=TWILIO_NUMBER,
             to=MY_NUMBER
            )
        print(message.sid)
