from twilio.rest import Client
import os
from dotenv import load_dotenv

# SECURITY: Load credentials from .env
load_dotenv("../.env")
TWILIO_SID = os.getenv("twilio_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("twilio_auth_token")
TWILIO_VIRTUAL_NUMBER = '+16075245651'  # Twilio-provided virtual number
TWILIO_VERIFIED_NUMBER = '+16034988677' # Verified recipient number


class NotificationManager:
    """Manages SMS notifications via Twilio API.

    Encapsulates notification logic (SMS sending) separately from
    business logic (flight searching) for cleaner architecture.
    """

    def __init__(self):
        # API: Initialize Twilio client with credentials
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Send SMS notification with flight deal alert.

        Args:
            message: SMS body text (max 160 characters recommended)
        """
        # API: Twilio SMS creation
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,  # Sender (Twilio number)
            to=TWILIO_VERIFIED_NUMBER,    # Recipient (must be verified in Twilio)
        )
        # Print message SID for confirmation (unique message identifier)
        print(message.sid)


