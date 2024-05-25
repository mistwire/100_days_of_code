import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

data = response.json()['iss_position']
print(data)

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
iss_position = (latitude, longitude)
print(iss_position)

# site for finding lat/long of things https://www.latlong.net/Show-Latitude-Longitude.html


