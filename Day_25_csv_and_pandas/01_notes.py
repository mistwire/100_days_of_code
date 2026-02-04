# EVOLUTION: From manual file parsing to pandas DataFrames

# =================================================================
# 1. MANUAL FILE PARSING (Day 2 style - cumbersome!)
# =================================================================
# with open("./weather_data.csv", mode="r") as f:
#     data = f.readlines()
#     print(data)

# =================================================================
# 2. CSV LIBRARY (Slightly better - still manual)
# =================================================================
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(i[1])
#     print(temperatures)
# This works but requires manual indexing, type conversion, etc.

# =================================================================
# 3. PANDAS (Modern Python data science standard!)
# =================================================================
# https://pandas.pydata.org/docs/
# DataFrame = spreadsheet with rows/columns, Series = single column/row
import pandas

# KEY CONCEPT: read_csv() automatically parses headers and creates DataFrame
data = pandas.read_csv("weather_data.csv")
print(type(data))  # <class 'pandas.core.frame.DataFrame'>

# PATTERN: Access column by name (returns Series - 1D data structure)
print(type(data["temp"]))  # <class 'pandas.core.series.Series'>
print(data["temp"])

# CONVERSION: DataFrame → Dictionary (useful for file I/O, Day 2 review)
data_dict = data.to_dict()
print(data_dict)

# CONVERSION: Series → List (for when you need iteration without pandas)
temp_list = data["temp"].to_list()
print(len(temp_list))

# PATTERN: Manual statistics vs pandas built-in methods
avg_temp = sum(temp_list) / (len(temp_list))
print(avg_temp)

# KEY CONCEPT: pandas statistical methods (much cleaner!)
# These work on Series: mean(), max(), min(), std(), sum(), count()
average = data["temp"].mean()  # Replaces sum()/len() pattern
print(average)

max_value = data["temp"].max()
print(max_value)

# PATTERN: Multiple column access syntaxes (both work)
print(data["condition"])
print(data.condition)  # Attribute syntax (works when column name is valid identifier)
print(data.condition[3])  # Access specific row within column

# FILTERING PATTERN: Boolean indexing - get rows matching condition
print(data[data["day"] == "Monday"])  # Returns DataFrame with matching rows

# Find row with highest temperature
print(data[data.temp == data.temp.max()])

# PATTERN: Chain operations - filter then extract column
monday = data[data.day == "Monday"]
print(monday.condition)  # Get condition column from Monday's data

# PATTERN: Math operations on Series (vectorized - applies to all rows)
monday = data[data.day == "Monday"]
# This calculates Fahrenheit for every row in monday DataFrame
print((monday.temp * 9/5) + 32)

# =================================================================
# 4. CREATE DataFrame FROM SCRATCH (not from CSV)
# =================================================================
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)

# PATTERN: Save DataFrame as CSV
data.to_csv('new_data.csv')

