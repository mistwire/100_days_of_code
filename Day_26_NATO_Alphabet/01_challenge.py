import random

# List Comprehensions Exercise 1
# You are going to write a List Comprehension to create a new list called squared_numbers. 
# This new list should contain every number in the list numbers but each number should be squared.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Write your 1 line code 👇 below:
squared_numbers = [x*x for x in numbers]
# Write your code 👆 above:
print(squared_numbers)

# List Comprehensions Exercise 2
list_of_strings = ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55']
# 🚨 Do  not change the code above
# TODO: Use list comprehension to convert the strings to integers 👇:
to_int = [int(x) for x in list_of_strings]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [x for x in to_int if x%2 == 0]
# Write your code 👆 above:
print(result)


# Dictionary Comprehension Exercise 1
# You are going to use Dictionary Comprehension to create a dictionary called result that takes 
# each word in the given sentence and calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result= {k:len(k) for k in sentence.split()}
print(result)



# Dictionary Comprehension Exercise 2
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred", "George"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {k:v for (k,v) in student_scores.items() if v >= 60}
print(passed_students)

# Dictionary Comprehension Exercise 3
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes
# each temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {k:((v * 9/5) + 32)  for k,v in weather_c.items() }
print(weather_f)


# Iterate over a Pandas dataframe
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dicts
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through df
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Loop through rows of a df
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)

