import smtplib
import requests
import datetime as dt
import time

# SECURITY NOTE: Credentials should be in .env file (see Day 35), not hardcoded!
my_email = "mistwire.test01@gmail.com"
password = "NotReallyMyPassword"
MY_LAT = 43.0203247
MY_LONG = -70.931396


def iss_isclose():
    """Check if ISS is currently above the observer's location (within ~5 degree radius)."""
    # API: Open Notify's real-time ISS position endpoint
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # KEY CONCEPT: Extract and convert latitude/longitude from API response
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # ALGORITHM: Check if ISS is within a degree range of observer location
    # (approximates distance; proper calculation would use Haversine formula)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_dark():
    """Check if it's currently dark (between sunset and sunrise)."""
    # API: sunrise-sunset.org provides daily sunrise/sunset times by location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # ISO 8601 format for easier parsing
    }
    # verify=False disables SSL certificate verification (only for testing/expired certs!)
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    # PATTERN: Extract hour from ISO timestamp string via string splitting
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # KEY CONCEPT: Use UTC for all time comparisons (ISS position is in UTC)
    time_now = dt.datetime.now(dt.timezone.utc)
    # It's dark if current time is after sunset OR before sunrise
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        print("it's dark!")
        return True


# PATTERN: Polling loop checks conditions periodically (similar to Day 28 Pomodoro)
while True:
    if iss_isclose() and is_dark():
        # KEY CONCEPT: SMTP context manager (with statement) ensures connection closes even if error occurs
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # PATTERN: starttls() upgrades connection to TLS encryption (required by Gmail)
            connection.starttls()
            # Authenticate with email and app password (not main account password!)
            connection.login(user=my_email, password=password)
            # PATTERN: Email format is "Subject:<subject>\n\n<body>"
            connection.sendmail(
                from_addr=my_email,
                to_addrs="chrisfwilliams@gmail.com",
                msg=f"Subject:ISS Alert, look up 👆\n\nISS is overhead")
    # PATTERN: Sleep reduces API load and prevents race conditions
    # 60 seconds = good balance between responsiveness and rate limits
    time.sleep(60)

