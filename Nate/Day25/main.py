# import csv
#
# with open('weather_data.csv', mode='r') as f:
#     data = csv.reader(f)
#     temps = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temps.append(int(temp))
#
# print(temps)

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# temp_f = (monday.temp * 1.8) + 32
# print(temp_f)
#
# print(data[data.temp == data.temp.max()])

color = data["Primary Fur Color"] == "Gray"

gray = data[data["Primary Fur Color"] == "Gray"]
# black = data["Primary Fur Color" == "Black"]
# red = data["Primary Fur Color" == "Cinnamon"]

color_counts = (data["Primary Fur Color"].value_counts())
color_counts.to_csv("colors.csv")