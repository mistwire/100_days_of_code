# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [n**2 for n in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)

# result = [n for n in numbers if n % 2 == 0]
# print(result)

# with open("file1.txt") as f:
#     list1 = f.readlines()
#     list1 = [line.rstrip() for line in list1]
#
# with open("file2.txt") as f:
#     list2 = f.readlines()
#     list2 = [line.rstrip() for line in list2]
#
# result = [int(number) for number in list1 if number in list2]
#
# print(list1)
# print(list2)
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# sen_list = sentence.split()
# print(sen_list)
#
# result = {word: len(word) for word in sen_list}
#
#
# print(result)

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


# Write your code 👇 below:
def convert(temp):
    return temp * 9/5 + 32


weather_f = {day:(convert(temp_c)) for (day, temp_c) in weather_c.items()}

print(weather_f)







