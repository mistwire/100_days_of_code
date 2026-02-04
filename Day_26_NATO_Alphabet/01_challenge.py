import random

# =================================================================
# LIST COMPREHENSIONS
# =================================================================

# Exercise 1: Transform each element (square the numbers)
# PATTERN: [expression for item in iterable]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Traditional way:
# squared_numbers = []
# for x in numbers:
#     squared_numbers.append(x * x)

# List comprehension (concise and readable):
squared_numbers = [x * x for x in numbers]
print(squared_numbers)

# Exercise 2a: Type conversion with comprehension
# PATTERN: [conversion_function(item) for item in iterable]
list_of_strings = ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55']
# Convert strings to integers using int() inside comprehension
to_int = [int(x) for x in list_of_strings]

# Exercise 2b: Filter with conditional
# PATTERN: [expression for item in iterable if condition]
# Keep only even numbers (x % 2 == 0)
result = [x for x in to_int if x % 2 == 0]
print(result)


# =================================================================
# DICTIONARY COMPREHENSIONS
# =================================================================

# Exercise 1: Create word-to-length mapping
# PATTERN: {key_expression: value_expression for item in iterable}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# For each word in sentence, create key=word, value=word length
result = {k: len(k) for k in sentence.split()}
# Result: {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, ...}
print(result)



# Exercise 2: Filter existing dictionary with comprehension
# Create dict with random scores for each student
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred", "George"]
student_scores = {student: random.randint(1, 100) for student in names}
# Result: {'Alex': 45, 'Beth': 92, ...}
print(student_scores)

# PATTERN: Filter dict with conditional
# {k: v for (k, v) in dict.items() if condition}
# Keep only students with score >= 60
passed_students = {k: v for (k, v) in student_scores.items() if v >= 60}
print(passed_students)

# Exercise 3: Transform dictionary values with comprehension
# Convert temperatures from Celsius to Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# PATTERN: Transform dict values
# {key: new_value_expression for key, value in dict.items()}
# Keep keys (day names), transform values (C to F)
# Formula: F = (C * 9/5) + 32
weather_f = {k: ((v * 9/5) + 32) for k, v in weather_c.items()}
print(weather_f)


# =================================================================
# PANDAS DATAFRAME ITERATION (Foundation for Day 26 NATO challenge)
# =================================================================
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# PATTERN: Loop through dictionary items
# .items() returns (key, value) tuples
for (key, value) in student_dict.items():
    # In this case, value is a list, not scalar
    print(value)

# Convert dict to DataFrame for structured data handling
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# PATTERN: Loop through DataFrame COLUMNS
# .items() on DataFrame returns (column_name, Series) tuples
for (key, value) in student_data_frame.items():
    print(key)      # Column name: 'student', 'score'
    print(value)    # Series: [Angela, James, Lily] or [56, 76, 98]

# PATTERN: Loop through DataFrame ROWS (most common for data processing)
# .iterrows() returns (index, row) tuples where row is a Series
# This is what we use for dictionary comprehension in NATO challenge
for (index, row) in student_data_frame.iterrows():
    print(index)        # Row number: 0, 1, 2
    print(row)          # Entire row as Series
    print(row.student)  # Access column by attribute name
    print(row.score)    # Can also use row["score"]

    # Conditional logic on rows
    if row.student == "Angela":
        print(row.score)

