import requests
from datetime import date

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "farroar"
TOKEN = "horsebatterystapler"

params = {
    "token": TOKEN,
    "username": "USERNAME",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=params)
# #response.raise_for_status()
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "farroar1",
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = str(date.today())
today_fmt = today.replace("-", "")

pixel_json = {
    "date": today_fmt,
    "quantity": "4",
}

pixel_endpoint = f"{pixela_graph_endpoint}/{graph_params['id']}"
# response = requests.post(url=pixel_endpoint, json=pixel_json, headers=headers)
# print(response.text)

update_pixel = {
    "quantity": "8"
}

response = requests.put(url=f"{pixel_endpoint}/{today_fmt}", json=update_pixel, headers=headers)
print(response.text)


