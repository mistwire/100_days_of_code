import pandas
import random

# For Loop version:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# List comprehension version:
new_list2 = [n + 1 for n in numbers]
print(new_list2)

name = "Angela"
new_list3 = [letter for letter in name]
print(new_list3)

# works on any iterable

new_list4 = [x*2 for x in range(1, 5)]
print(new_list4)

# Conditional List Comprehension:
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# get list of names with 4 or fewer letters
short_names = [name for name in names if len(name) < 5]
print(short_names)

# uppercase all names with 5 or more letters
long_names_upper = [x.upper() for x in names if len(x) > 5]
print(long_names_upper)

# 233 coding exercise
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [i**2 for i in numbers]
print(squared_numbers)

# 234 coding exercise
result = [x for x in numbers if x % 2 == 0]
print(result)

# Dictionary comprehensions:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student: random.randint(0, 100) for student in names}
print(student_score)
students_dict = {'Alex': 37, 'Beth': 72, 'Caroline': 99, 'Dave': 38, 'Eleanor': 59, 'Freddie': 28}

passed_students = {k: v for (k, v) in students_dict.items() if v >= 60}
print(passed_students)

# Coding exercise 238
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:

result = {k: len(k) for k in sentence.split()}
print(result)

# Coding exercise 239
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# convert temp to F
# Write your code 👇 below:
weather_f = {k: (v * 9/5) + 35 for k, v in weather_c.items()}
print(weather_f)

# 240 How to Iterate over a Pandas DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily", "Chris"],
    "score": [45, 65, 94, 100]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through a data frame
for (key, value) in student_df.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row.score) # Each row is a pandas Series

