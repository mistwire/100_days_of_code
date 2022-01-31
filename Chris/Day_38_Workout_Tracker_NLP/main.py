import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv("../.env")
GENDER = "Male"
WEIGHT_KG = "109"
HEIGHT_CM = "200"
AGE = "48"
APP_ID = os.getenv("nutritionix_apiID")
API_KEY = os.getenv("nutritionix_apikey")
sheety_token = os.getenv("sheety_workout_token")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/workoutTracking/workouts"

sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}
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
today = datetime.datetime.now()
r_nutritionix = requests.post(url=exercise_endpoint, json=exercise_request_body, headers=nutritionix_headers)
exercises = r_nutritionix.json()['exercises']
for i in exercises:
    post_body = {
        "workout": {
            "date": today.strftime("%m/%d/%y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": i["name"].title(),
            "duration": i['duration_min'],
            "calories": i["nf_calories"],
        }
    }
    r = requests.post(url=sheety_endpoint, json=post_body, headers=sheety_headers)
    print(r.json())
