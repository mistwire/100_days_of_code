# Day 37: Habit Tracker -- HTTP CRUD Operations & REST APIs

## What You Learned
You worked with the Pixe.la API to build a pixel-based habit tracker. This introduced HTTP CRUD operations (Create, Read, Update, Delete) and REST principles. Unlike previous days' GET-only usage, you now used POST, PUT, and DELETE to modify data on remote servers.

---

## Key Concepts

### 1. CRUD Operations & HTTP Methods
REST APIs use different HTTP methods for different operations:

```python
import requests

# CREATE: Use POST to create new resources
new_resource = {
    "field": "value"
}
response = requests.post(url=endpoint, json=new_resource, headers=headers)

# READ: Use GET to fetch existing resources
response = requests.get(url=endpoint, headers=headers)

# UPDATE: Use PUT to replace entire resource or PATCH to partial update
response = requests.put(url=endpoint, json=updated_data, headers=headers)

# DELETE: Remove resource
response = requests.delete(url=endpoint, headers=headers)
```

**Why**: RESTful design uses HTTP verbs semantically (POST = create, GET = read, etc.), making APIs intuitive and consistent.

### 2. Authentication with Custom Headers
Some APIs require authentication via headers instead of query parameters:

```python
TOKEN = "my_secret_token"
headers = {"X-USER-TOKEN": TOKEN}

response = requests.post(url=endpoint, json=data, headers=headers)
```

**Why**: Headers are more secure than URLs (not logged in browser history) and support various auth schemes.

### 3. API Endpoints as Resource Hierarchies
Building URLs to represent resource relationships:

```python
pixela_endpoint = "https://pixe.la/v1/users"

# Create user
r = requests.post(url=pixela_endpoint, json=user_params)

# Create graph for user
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Add pixel to graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
r = requests.post(url=pixel_endpoint, json=body, headers=headers)

# Delete pixel from graph
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20220127"
r = requests.delete(url=pixel_delete_endpoint, headers=headers)
```

**Why**: URLs represent resource hierarchy (users > user > graphs > graph > pixels). Changing the verb (POST/PUT/DELETE) operates on the same resource in different ways.

### 4. Date String Formatting
Converting Python datetime to API-required format:

```python
import datetime

today = datetime.now()
# strftime: "string format time"
date_string = today.strftime("%Y%m%d")  # "20240204"

# Pixe.la requires dates in YYYYMMDD format for pixel operations
pixel_date = "20220127"  # January 27, 2022
```

**Why**: APIs often require specific date formats. `strftime()` converts flexibly without manual string building.

### 5. Posting Complex JSON Structures
Sending nested JSON objects to APIs:

```python
# Simple structure
body = {
    "date": "20220127",
    "quantity": "30"
}
response = requests.post(url=endpoint, json=body, headers=headers)

# Nested structure (some APIs require this)
nested_body = {
    "price": {  # Wrapper object
        "iataCode": "BOS"
    }
}
response = requests.put(url=endpoint, json=nested_body, headers=headers)
```

**Why**: Some APIs group related fields in objects to organize data hierarchically.

### 6. Interactive User Input in API Calls
Getting data from user and using it in API requests:

```python
quantity = input("How many minutes did you study today?: ")
body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity
}
response = requests.post(url=endpoint, json=body, headers=headers)
```

**Why**: Data-driven applications respond to user input, not hardcoded values.

### 7. Graph-Based Tracking
Understanding pixel graphs as a data visualization:

```python
# Pixe.la creates a visual calendar:
# - Each pixel = one day
# - Color intensity = quantity value
# - Build consistent habits by filling pixels regularly
```

**Why**: Visual progress (filled calendar) is motivating for habit tracking vs. abstract numbers.

### 8. API Documentation Reading
Understanding complex APIs by reading their docs:

```python
# From https://docs.pixe.la/:
# - POST to create user/graph/pixel
# - PUT to update pixel
# - DELETE to remove pixel
# Each endpoint has specific required/optional parameters

# Always check:
# - Authentication method (headers, query params, API key)
# - Request body format (JSON vs form data)
# - Response format
# - Rate limits
```

**Why**: Well-designed APIs have detailed docs. Learning to read them is a critical skill.

---

## Common Pitfalls
- **Wrong date format**: Pixe.la uses YYYYMMDD (no dashes); using "2022-01-27" will fail.
- **Forgetting headers in POST/PUT/DELETE**: Pixe.la requires authentication header for most operations.
- **Not checking response status**: Always use `.raise_for_status()` or check `response.status_code`.
- **Confusing PUT vs PATCH**: PUT replaces entire resource; PATCH modifies only specified fields.
- **Mixing endpoints**: Different endpoints require different headers or body structures.
- **Not reading error messages**: API responses include helpful error messages; print `response.text` to debug.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 28 (Pomodoro)** | Similar time-tracking concept (minutes studied vs. work intervals) |
| **Day 33 (ISS Tracker)** | GET requests; this shows POST/PUT/DELETE |
| **Day 35 (Weather API)** | Environment variables for API keys |
| **Day 36 (Stock Tracker)** | Multiple API integration; conditional logic |
| **Day 38 (Workout Tracker)** | Similar tracking pattern; multiple APIs |
| **Day 39-40 (Flight Deals)** | Sheety API for data storage; POST/PUT requests |

---

## Before You Move On

Make sure you can:
- [ ] Use requests.post(), requests.put(), and requests.delete()
- [ ] Understand HTTP CRUD operations and when to use each
- [ ] Pass custom headers for authentication (X-USER-TOKEN, Authorization, etc.)
- [ ] Build endpoint URLs with variables (f-strings for user IDs, resource IDs)
- [ ] Format dates using strftime() (YYYYMMDD, MM/DD/YYYY, etc.)
- [ ] Parse and navigate API documentation
- [ ] Send JSON-formatted request bodies with requests.post() and requests.put()
- [ ] Handle API responses and errors
- [ ] Understand REST principles (resource hierarchy, HTTP verbs)

---

## Practice Prompt
Build a **Book Reading Tracker**: Create a program that:
1. Uses Pixe.la to create a graph for "pages read per day"
2. Prompts user daily: "How many pages did you read today?"
3. Posts the data to Pixe.la (updates pixel for today)
4. Displays a message: "Great job! You've read X pages this month"
5. Allows users to:
   - View their reading graph (URL to pixe.la)
   - Update previous days (PUT request with different dates)
   - Delete erroneous entries (DELETE request)
   - Set a daily goal (e.g., "Read 50 pages per day")

Bonus: Integrate with Google Books API to log book titles; store completed books in a CSV.
