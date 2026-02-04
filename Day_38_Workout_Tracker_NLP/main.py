import os
import requests
from dotenv import load_dotenv
import datetime

# SECURITY: Load API keys from .env file
load_dotenv("../.env")

# User biometric data (used by Nutritionix to calculate calorie burn accurately)
# Different people burn different calories for same exercise based on these factors
GENDER = "Male"
WEIGHT_KG = "109"
HEIGHT_CM = "200"
AGE = "48"

# API credentials from .env
APP_ID = os.getenv("nutritionix_apiID")
API_KEY = os.getenv("nutritionix_apikey")
sheety_token = os.getenv("sheety_workout_token")

# API endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ba4e14c62c9f1f5d24852c1ab5b3a5a6/workoutTracking/workouts"

# API 1: Sheety (Google Sheets integration)
# Authorization: Bearer token in header
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

# API 2: Nutritionix (Exercise NLP and calorie estimation)
# Custom headers for Nutritionix authentication
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

# Get user input and build API request
# KEY CONCEPT: Natural Language Processing
# User enters free-form text like "I ran 5 miles" or "Did 30 pushups"
# Nutritionix API understands natural language and extracts structured data
exercise_request_body = {
    "query": input("Tell me which exercise you did: "),
    # These biometrics are sent with every request for accurate calorie calculation
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Get current date/time
today = datetime.datetime.now()

# API 1: Send exercise query to Nutritionix
# Nutritionix parses natural language and returns structured exercise data
r_nutritionix = requests.post(url=exercise_endpoint, json=exercise_request_body, headers=nutritionix_headers)
print(r_nutritionix.json())

# PATTERN: Extract array from API response
# Response format: {"exercises": [{...}, {...}, ...]}
exercises = r_nutritionix.json()['exercises']

# PATTERN: Loop over API results and build requests for another API
# Each exercise from Nutritionix becomes a row in the Google Sheet
for i in exercises:
    # Build request body for Sheety API (Google Sheets format)
    # KEY CONCEPT: Transform Nutritionix output to match Sheety input
    post_body = {
        "workout": {
            # Date/time formatting for Google Sheets
            "date": today.strftime("%m/%d/%y"),      # "02/04/24"
            "time": today.strftime("%H:%M:%S"),      # "14:30:45"
            # Transform exercise name: "running" -> "Running" (title case for readability)
            "exercise": i["name"].title(),
            # Duration and calories from Nutritionix
            "duration": i['duration_min'],           # Integer: 30
            "calories": i["nf_calories"],            # Float: 312.5
        }
    }

    # API 2: Post workout data to Sheety (Google Sheets)
    # This writes the exercise data as a new row in the spreadsheet
    r = requests.post(url=sheety_endpoint, json=post_body, headers=sheety_headers)
    print(r.json())
