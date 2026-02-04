# Day 38: Workout Tracker with NLP -- Natural Language Processing & Dual API Integration

## What You Learned
You combined natural language processing (NLP) with two APIs (Nutritionix and Sheety) to build a workout tracker that accepts free-form text input (e.g., "I ran 3 miles") and automatically logs exercise data to a Google Sheet. This demonstrates how APIs can handle complex, human-like input instead of requiring structured forms.

---

## Key Concepts

### 1. Natural Language Processing (NLP) for Exercise Recognition
The Nutritionix API accepts free-form text and parses exercise descriptions:

```python
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_request_body = {
    "query": input("Tell me which exercise you did: "),
    # User enters: "I ran 3 miles" or "Did 50 pushups"
    # API understands natural language and extracts structured data
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

r_nutritionix = requests.post(url=exercise_endpoint, json=exercise_request_body, headers=nutritionix_headers)
exercises = r_nutritionix.json()['exercises']
# API returns: [{name: "running", duration_min: 30, nf_calories: 300}, ...]
```

**Why**: Users describe exercises naturally; NLP extracts structure. Avoids dropdown menus or complex forms.

### 2. User Biometric Data for Accurate Calculations
Exercise calorie burn varies by person; APIs use biometrics for accuracy:

```python
GENDER = "Male"
WEIGHT_KG = "109"
HEIGHT_CM = "200"
AGE = "48"

# These parameters are sent to Nutritionix API
# Nutritionix calculates calorie burn based on:
# - Exercise type and duration
# - User's gender, weight, height, age (affects metabolism)

# Without biometrics: 30-min run = ~300 calories (generic)
# With biometrics: Same run for 109kg, 200cm, 48yo male = different value
```

**Why**: Calorie expenditure is highly individual. Accounting for biometrics improves accuracy.

### 3. Parsing Complex Nested API Responses
Real APIs return deeply nested data; you must navigate hierarchies:

```python
response_json = r_nutritionix.json()
exercises = response_json['exercises']  # Array of exercise objects

for exercise in exercises:
    name = exercise["name"]              # "running"
    duration = exercise['duration_min']  # 30
    calories = exercise["nf_calories"]   # 312.5
```

**Why**: Complex data requires hierarchical access. Practice navigating JSON ensures you can work with any API.

### 4. Iterating Over API Results & Building Request Bodies
Looping over API results to create requests for another API:

```python
exercises = r_nutritionix.json()['exercises']

for i in exercises:
    # Extract data from Nutritionix response
    post_body = {
        "workout": {  # Nested structure required by Sheety
            "date": today.strftime("%m/%d/%y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": i["name"].title(),        # "Running"
            "duration": i['duration_min'],        # 30
            "calories": i["nf_calories"],         # 312
        }
    }
    # Post to Sheety API (Google Sheets)
    r = requests.post(url=sheety_endpoint, json=post_body, headers=sheety_headers)
```

**Why**: Chaining APIs converts data between formats. Nutritionix output becomes Sheety input.

### 5. Formatting Data for Readability
Converting raw API data into user-friendly formats:

```python
# Raw data: "running" (lowercase)
# User-friendly: "Running" (title case)
"exercise": i["name"].title()

# Raw time: 31.4 minutes
# User-friendly: Store as integer or round
"duration": i['duration_min']
```

**Why**: Presentation matters. Users expect "Running", not "running"; whole numbers, not decimals.

### 6. Using String Methods for Text Transformation
Python string methods clean up API data:

```python
name = "running"
name.title()        # "Running"
name.upper()        # "RUNNING"
name.capitalize()   # "Running"

# Full-text example:
i["name"].title()   # "Running" instead of "running"
```

**Why**: Consistent formatting improves readability in logs/sheets.

### 7. Handling Date/Time Components Separately
Different APIs expect different date/time formats:

```python
today = datetime.datetime.now()

# Nutritionix might not need time (they only parse exercise from text)
# Sheety expects both date and time:
date_str = today.strftime("%m/%d/%y")      # "02/04/24"
time_str = today.strftime("%H:%M:%S")      # "14:30:45"

post_body = {
    "workout": {
        "date": date_str,
        "time": time_str,
        "exercise": "Running",
        "duration": 30,
        "calories": 312,
    }
}
```

**Why**: Different systems have different format requirements. Separate concern for clarity.

### 8. Authorization with Bearer Tokens
Modern APIs often use Bearer tokens in Authorization headers:

```python
sheety_token = os.getenv("sheety_workout_token")
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

response = requests.post(url=sheety_endpoint, json=post_body, headers=sheety_headers)
```

**Why**: Bearer tokens are stateless, scalable, and work across multiple requests without session management.

---

## Common Pitfalls
- **Not handling empty API responses**: Exercise name might be None; check before using `.title()`.
- **Forgetting biometric parameters**: Nutritionix requires gender, weight, height, age for accurate calories.
- **Wrong header format**: Sheety uses `Authorization: Bearer <token>`, not `X-USER-TOKEN`.
- **Hardcoding API endpoints**: Storing as constants allows easy updates if APIs change.
- **Not encoding special characters**: If exercise name has accents, ensure UTF-8 encoding.
- **Mismatched date formats**: Sheety expects MM/DD/YY; Nutritionix might expect different format.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 35 (Weather API)** | Environment variables for API keys; multiple APIs |
| **Day 36 (Stock Tracker)** | Multi-API integration; looping over results |
| **Day 37 (Habit Tracker)** | POST requests; custom headers for authentication |
| **Day 39-40 (Flight Deals)** | Combining multiple APIs; data transformation |
| **Day 25 (CSV/Pandas)** | Writing data to spreadsheets (but here via API instead of local file) |

---

## Before You Move On

Make sure you can:
- [ ] Send natural language queries to NLP APIs (Nutritionix, OpenAI, etc.)
- [ ] Parse deeply nested JSON responses from complex APIs
- [ ] Loop over API results and build requests for a second API
- [ ] Format dates/times using strftime() with different patterns
- [ ] Handle Bearer token authentication in headers
- [ ] Transform text data using Python string methods (`.title()`, `.capitalize()`, etc.)
- [ ] Understand how APIs communicate with each other (output of one = input of another)
- [ ] Handle edge cases (missing fields, empty responses, wrong data types)

---

## Practice Prompt
Build a **Comprehensive Health Tracker**: Create a program that:
1. Accepts three types of input:
   - Exercise: "I ran 5 miles" → Uses Nutritionix API
   - Food: "Had a chicken sandwich" → Uses Nutritionix API for nutrition
   - Sleep: "Slept 8 hours" → Uses your own format
2. Stores all data in Google Sheets (via Sheety API) with columns:
   - Date, Time, Type (exercise/food/sleep), Details, Duration/Amount, Calories (if applicable)
3. Calculates daily/weekly stats:
   - Total calories burned from exercise
   - Total calories consumed from food
   - Net calories (consumed - burned)
   - Average sleep hours
4. Sends weekly email summary with trends

Bonus: Integrate with Google Chart API to visualize trends; add goals (e.g., "Burn 2000 calories/day") and track progress.
