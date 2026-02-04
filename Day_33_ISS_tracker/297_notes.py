# What is an API?
# KEY CONCEPT: APIs expose data/functionality over HTTP; requests library abstracts the complexity

import requests

# API: Making a GET request to Open Notify's ISS position endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # Prints Response object with status_code, headers, etc.
print(response.json())  # Parse JSON string into Python dict
print(response.text)  # Raw response body as string

new_dict = response.json()  # Store parsed data

print(new_dict)
print(type(new_dict))  # <class 'dict'>

# KEY CONCEPT: .raise_for_status() raises HTTPError if status != 2xx
# This prevents silent failures when the API is down or rejects the request
# https://docs.python-requests.org/en/latest/
print(response.raise_for_status())


