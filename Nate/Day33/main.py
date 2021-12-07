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
    lat = int(float(data['iss_position']['latitude']))
    long = int(float(data['iss_position']['latitude']))
    location = (lat, long)
    return location


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


if is_night():
    iss_position = get_iss_pos()
    my_position = (int(MY_LAT), int(MY_LONG))

    if iss_position == my_position:
        send_mail('me@email.com', "look up")


