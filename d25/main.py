
import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     # del temperatures[0]
#
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
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
# print((x * 1.8) + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)