# HTTP Requests using https://pixe.la/ to create a habit tracker
# requests.get() requests.post() requests.put() requests.delete()

import requests

USERNAME = "mistwire"
TOKEN = "awkjb2u3jaubao4jn3qu4i29ou3b"

# Step 1. Create user account:
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# send using json keyword (instead of params):
# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)
# {"message":"Success. Let's visit https://pixe.la/@mistwire , it is your profile page!","isSuccess":true}

# Step 2. Create a graph definition:

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "minutes",
    "type":


}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
r = requests.post(url=graph_endpoint, )