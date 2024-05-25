import smtplib
import requests
import datetime as dt
import time

my_email = "mistwire.test01@gmail.com"
password = "NotReallyMyPassword"
MY_LAT = 43.0203247
MY_LONG = -70.931396


def iss_isclose():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now(dt.timezone.utc)
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        print("it's dark!")
        return True


while True:
    if iss_isclose() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="chrisfwilliams@gmail.com",
                msg=f"Subject:ISS Alert, look up 👆\n\nISS is overhead")
    time.sleep(60)

