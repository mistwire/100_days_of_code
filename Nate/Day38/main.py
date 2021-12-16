import requests
import datetime as dt
import os

NT_API_KEY = os.environ.get("NT_API_KEY")
NT_API_ID = os.environ.get(("NT_API_ID"))
NT_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")


def get_workout(query):
    headers = {
        'x-app-id': NT_API_ID,
        'x-app-key': NT_API_KEY,
        'x-remote-user-id': '0'
    }

    params = {
        'query': query,
        'gender': "male",
        'weight_kg': 75,
        'height_cm': 178,
        'age': 41
    }
    response = requests.post(url=NT_API_ENDPOINT, headers=headers, json=params)
    response.raise_for_status()
    return response.json()


now = dt.datetime.now()
today_fmt = now.strftime("%m/%d/%Y")
time_fmt = now.strftime("%I:%M")

exercise = input("What was your activity? ")
result = get_workout(exercise)

for exercise in result['exercises']:
    exercise_data = {
        "workout": {
            "date": today_fmt,
            "time": time_fmt,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.post(url=SHEETY_API_ENDPOINT, json=exercise_data)



