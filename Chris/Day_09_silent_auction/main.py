# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     }
# print(programming_dictionary["Bug"])

# # Add new item to dict
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# # Create an empty dict
# empty_dict = {}

# # Wipe an existing dict
# # programming_dictionary = {}

# # Edit an item in a dict 
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# # Loop through a dict
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key]>= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)