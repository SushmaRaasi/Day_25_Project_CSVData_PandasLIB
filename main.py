"""
with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    """
"""import csv

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temp = int(row[1])
            temperature.append(temp)
    print(temperature)
"""

import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

"""data_dict = data.to_dict()
print(data_dict)"""

"""temp_list = data["temp"].to_list()
length = len(temp_list)
sum_list = sum(temp_list)
Average = round(sum_list / length)
print(Average)"""

#print(data["temp"].mean())

max_temp = data["temp"].max()

# get data in columns

"""print(data["condition"])
print(data.condition)"""

# get data in rows
#print(data[data["day"] == "Monday"])

# get max temp row
"""
print(data[data["temp"] == max_temp])
monday = data[data["day"] == "Monday"]
#print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)"""


# Creating DataFrame

data_dict = {
    "names": ["sri", "sushma", "raasi"],
    "numbers": [1, 2, 3]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")









