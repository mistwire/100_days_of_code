import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [
        data["Primary Fur Color"].value_counts()["Gray"],
        data["Primary Fur Color"].value_counts()["Black"],
        data["Primary Fur Color"].value_counts()["Cinnamon"],
    ]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

"""
all in one line :-)
data["Primary Fur Color"].value_counts().to_csv("data.csv") 
"""