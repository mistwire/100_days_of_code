import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")

GENDER = "Male"
WEIGHT_KG = "109"
HEIGHT_CM = "200"
AGE = "48"

APP_ID = os.getenv("nutritionix_apiID")
API_KEY = os.getenv("nutritionix_apikey")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_request_body = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

r = requests.post(url=exercise_endpoint, json=exercise_request_body, headers=nutritionix_headers)
print(r.json())

