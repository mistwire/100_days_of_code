# HTTP Requests using https://pixe.la/ to create a habit tracker
# requests.get() requests.post() requests.put() requests.delete()
import requests
from datetime import datetime
USERNAME = "mistwire"
TOKEN = "awkjb2u3jaubao4jn3qu4i29ou3b"
GRAPHID = "graph1"
# Step 1. Create user account:
pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# send using json keyword (instead of params):
# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)
# {"message":"Success. Let's visit https://pixe.la/@mistwire , it is your profile page!","isSuccess":true}
# Step 2. Create a graph definition:
graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": TOKEN}
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(r.text)
# {"message":"Success.","isSuccess":true}

# Step 3. Post a pixel
today = datetime.now()
# strftime method: https://www.w3schools.com/python/python_datetime.asp
# print(today.strftime("%Y%m%d"))
body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you study today?: "),
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
r = requests.post(url=pixel_creation_endpoint, json=body, headers=headers)
print(r.text)
# Use PUT to update a pixel https://docs.pixe.la/entry/put-pixel
# Use DELETE to delete a pixel  https://docs.pixe.la/entry/delete-pixel
# pixel_deletion_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20220127"
# r = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# print(r.text)

