import requests
from datetime import datetime
MY_LAT = 42.856510
MY_LONG = -70.933517


def send_mail(email, contents):
    print(email)
    print(contents)


def get_iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    lat = float(data['iss_position']['latitude'])
    long = float(data['iss_position']['longitude'])
    location = (lat, long)
    return location


def iss_overhead():
    if is_night():
        current_iss_pos = get_iss_pos()
        iss_lat = current_iss_pos[0]
        iss_long = current_iss_pos[1]

        if (MY_LAT - 5) <= iss_lat <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_long <= (MY_LONG + 5):
            return True


def is_night():
    params = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    data = response.json()
    sunset_raw = data['results']['sunset'].split('T')[1]
    sunset_hour = sunset_raw.split(':')[0]
    adj_sunset_hour = int(sunset_hour) - 5

    now = datetime.now()
    if now.hour > adj_sunset_hour:
        return True


if iss_overhead():
    send_mail('me@email.com', "look up")
