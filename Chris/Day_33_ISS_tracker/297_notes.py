# What is an API?

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.json())
print(response.text)

new_dict = response.json()

print(new_dict)
print(type(new_dict))



