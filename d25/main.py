#
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     # del temperatures[0]
#
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
#
# print(data)
# average_temp = data.temp.mean()
# max_temp = data.temp.max()
# # print(round(average_temp, 2))
# # print(max_temp)
# # print(data[data["day"] =="Monday"])
# #
# # print(data[data.temp == data.temp.max()])
# #
#
# x = int(data.temp[data.day == "Monday"])
#
# # print((x * 1.8) + 32)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

# import pandas
import pandas
import pandas

# data = pd.read_csv('squirrel_data.csv', usecols=['Unique Squirrel ID', 'Age', 'Primary Fur Color', 'Highlight Fur Color'])
data = pandas.read_csv('squirrel_data.csv', usecols=['Primary Fur Color'])
print(data)


selected_animals = data[data['Primary Fur Color'] == "Gray"].count()
selected_animals1 = len(data[data['Primary Fur Color'] == "Gray"])
selected_animals2 = len(data[data['Primary Fur Color'] == "Cinnamon"])
selected_animals3 = len(data[data['Primary Fur Color'] == "Black"])
print(selected_animals)
print(selected_animals2)

data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
             "Count": [selected_animals1, selected_animals2, selected_animals3]
}

df = pandas.DataFrame(data_dict)
df.to_csv(("squirrel_count.csv"))

selected = data.groupby('Primary Fur Color').count()
# selected = data[data['Primary Fur Color'] == "Gray" or "Black" or "Cinanamon"]
print(f"\n\n{selected}")

