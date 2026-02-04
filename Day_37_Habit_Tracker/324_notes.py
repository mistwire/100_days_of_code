# API: Pixe.la - Pixel-based habit tracking visualization
# HTTP Methods Demonstrated:
# - requests.post()   = CREATE resource (user, graph, pixel)
# - requests.put()    = UPDATE existing resource
# - requests.delete() = DELETE resource
# https://docs.pixe.la/

import requests
from datetime import datetime

# Configuration
USERNAME = "mistwire"
TOKEN = "awkjb2u3jaubao4jn3qu4i29ou3b"  # SECURITY: Should be in .env!
GRAPHID = "graph1"

# API base endpoint for Pixe.la users
pixela_endpoint = "https://pixe.la/v1/users"

# Step 1. Create user account (commented because already done):
# KEY CONCEPT: HTTP POST creates new resources on the server
# user_params = {
#     "token": TOKEN,                    # User's secret token (like password)
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",      # Required by Pixe.la
#     "notMinor": "yes",                 # Must agree to TOS
# }
# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)
# Response: {"message":"Success. Let's visit https://pixe.la/@mistwire ...", "isSuccess":true}

# Step 2. Create a graph definition:
# PATTERN: Building endpoint URL with variables (f-string)
graph_config = {
    "id": "graph1",           # Unique identifier for this graph
    "name": "Study Graph",    # Display name
    "unit": "minutes",        # Unit of measurement
    "type": "int",            # Data type
    "color": "ajisai",        # Pixel color (Pixe.la provides color names)
}

# KEY CONCEPT: Authentication via custom header (not query parameter)
# Pixe.la requires X-USER-TOKEN header with user's token
headers = {"X-USER-TOKEN": TOKEN}

# Create graph (commented because already done):
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(r.text)
# Response: {"message":"Success.","isSuccess":true}

# Step 3. Post a pixel (add today's data):
today = datetime.now()

# PATTERN: Use strftime() to format date for API
# Pixe.la requires YYYYMMDD format (e.g., "20240204")
# Format codes: %Y=year, %m=month, %d=day (both 2-digit, zero-padded)
# See: https://www.w3schools.com/python/python_datetime.asp
body = {
    "date": today.strftime("%Y%m%d"),  # "20240204"
    "quantity": input("How many minutes did you study today?: "),
}

# PATTERN: Resource hierarchy in URL
# {base}/v1/users/{username}/graphs/{graphid}
# This represents: user > their graphs > specific graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

# HTTP POST: Add new pixel to graph (creates data for today)
r = requests.post(url=pixel_creation_endpoint, json=body, headers=headers)
print(r.text)

# Pixel visualization: https://pixe.la/@mistwire
# Each pixel represents a day; color intensity = quantity value

# EXAMPLE: Update a pixel with PUT method
# This would change a previous day's data:
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20240203"
# r = requests.put(url=pixel_update_endpoint, json={"quantity": "45"}, headers=headers)
# https://docs.pixe.la/entry/put-pixel

# EXAMPLE: Delete a pixel with DELETE method
# This would remove a day's data entirely:
# pixel_deletion_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20220127"
# r = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# https://docs.pixe.la/entry/delete-pixel

