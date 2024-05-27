# the slow cumbersome way
# with open("./weather_data.csv", mode="r") as f:
#     data = f.readlines()
#     print(data)

# with csv library create a list of all the temperatures
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(i[1])
#     print(temperatures)


# and then there's Pandas!
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html 
# DataFrame = excel spreadsheet, Series = row in spreadsheet 
import pandas 

data = pandas.read_csv("weather_data.csv")
print(type(data))
# get a single column:
print(type(data["temp"]))
print(data["temp"])

# turn dataframe into a dictionary:
data_dict = data.to_dict()
print(data_dict)

# turn series into a list:
temp_list = data["temp"].to_list()
print(len(temp_list))

avg_temp = sum(temp_list) / (len(temp_list))
print(avg_temp)

# OR

average = print(data["temp"].mean())
print(average)

max_value = print(data["temp"].max())
print(max_value)

# Get data in column
print(data["condition"])
# alternately 
print(data.condition)
print(data.condition[3])

# Get data in a row
print(data[data["day"] == "Monday"])

# Print the row of data which had the highest temp
print(data[data.temp == data.temp.max()])

# Get a row & pull 1 column's info out
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Monday's temp to Fahrenheit
monday = data[data.day == "Monday"]
print((monday.temp * 9/5) + 32)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
# Save as a csv file:
data.to_csv('new_data.csv')

