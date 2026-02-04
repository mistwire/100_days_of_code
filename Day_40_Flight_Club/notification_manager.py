import smtplib
from twilio.rest import Client
import os
from dotenv import load_dotenv

# SECURITY: Load credentials
load_dotenv("../.env")
TWILIO_SID = os.getenv("twilio_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("twilio_auth_token")
TWILIO_VIRTUAL_NUMBER = '+16075245651'
TWILIO_VERIFIED_NUMBER = '+16034988677'

# Gmail SMTP credentials
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "mistwire.test01@gmail.com"
MY_PASSWORD = "Severe-Merchant-Peace-10"  # SECURITY: Should be in .env!


class NotificationManager:
    """Manages notifications via SMS (Twilio) and Email (SMTP).

    Supports both single SMS alerts and bulk email notifications.
    """

    def __init__(self):
        # Initialize Twilio client
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Send SMS notification via Twilio."""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        """Send email notifications to multiple recipients.

        Args:
            emails: List of recipient email addresses
            message: Email body text (flight deal details)
            google_flight_link: URL to Google Flights for booking
        """
        # PATTERN: Use context manager for SMTP connection
        # 'with' statement ensures connection closes even if exception occurs
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            # PATTERN: Upgrade to TLS encryption (Gmail requires this)
            connection.starttls()
            # Authenticate with Gmail
            connection.login(MY_EMAIL, MY_PASSWORD)
            # PATTERN: Loop to send individual emails to each subscriber
            for email in emails:
                # PATTERN: Email format requires "Subject:..." header
                # Encode to UTF-8 to handle special characters (emojis, accents)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )