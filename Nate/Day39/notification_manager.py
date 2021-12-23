from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = "AC9f71e683a403031c1c5a6dc4ec10959a"
TWILIO_NUMBER = "+15304831979"
MY_NUMBER = "+13039173568"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
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
