# import csv
#
# # with open("weather_data.csv") as f:
# #     data = f.readlines()
# #
# # print(data)
#
# # with open("weather_data.csv") as f:
# #     data = csv.reader(f)
# #     print(data)  # creates csv object
# #     for row in data:
# #         print(row)  # each row is a list
#
# # Extract all temps into a new list from weather_data.csv
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temps = []
#     for row in data:
#         if row[1] != 'temp':
#             temps.append(int(row[1]))
#
#     print(temps)
# # This is a bunch of faff - MUCH easier to use pandas!!! :-)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))  # get back a Dataframe object (think 1 Excel spreadsheet)
# print(data)  # So pretty!
# print(type(data["temp"]))  # A Series is a column (also a list)
# print(data["temp"])  # Get 1 column
#
# data_dict = data.to_dict()
# print(data_dict)  # Can work with this as a dict now
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# print(len(temp_list))
#
# # TODO: Work out avg temp from list of temps
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# # OR use the pandas
# print(data['temp'].mean())
#
# # TODO: find max value using pandas data Series methods
# print(data['temp'].max())
#
# # Get data in columns - can access data via column name:
# print(data.condition)  # pandas reads the columns!
#
# # Get a row
# print(data[data.day == "Monday"])
#
# # TODO: pull out row where temp was max
# print(data[data.temp == data.temp.max()])
#
# # Use dot notation with variables and 'methods' !
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # TODO: Get monday temp and convert to Fahrenheit:
# print((monday.temp * 1.8) + 32)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

# Read data from squirrel csv
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data['Primary Fur Color']
squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [0, 0, 0]
}
for color in colors:
    if color == "Gray":
        squirrel_dict["Count"][0] += 1
    elif color == "Cinnamon":
        squirrel_dict["Count"][1] += 1
    elif color == "Black":
        squirrel_dict["Count"][2] += 1

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")
