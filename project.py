# Primary Fur Color

import pandas

data = pandas.read_csv("Squirrel_Data.csv")
"""colors = data["Primary Fur Color"]
colors_list = colors.to_list()
gray = 0
black = 0
cinnamon = 0
for color in colors_list:
    if color == "Gray":
        gray += 1
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1
    else:
        pass
print(f"Gray: {gray}, Black: {black}, Cinnamon: {cinnamon}")"""
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")





