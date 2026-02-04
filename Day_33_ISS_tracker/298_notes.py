import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # PATTERN: Always check status before using .json()

data = response.json()
print(data)  # Full response includes 'iss_position' and 'timestamp'

# KEY CONCEPT: Extracting nested values from JSON using chained dictionary access
data = response.json()['iss_position']
print(data)  # {'latitude': '...' , 'longitude': '...'}

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
iss_position = (latitude, longitude)  # PATTERN: Store extracted values to avoid repeated API calls
print(iss_position)

# NOTE: Inefficient to call response.json() 3 times; should parse once and reuse
# Better approach shown in 301_iss_notifier.py
# site for finding lat/long of things https://www.latlong.net/Show-Latitude-Longitude.html


