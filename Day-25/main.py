# # data =[]
# with open('weather_data.csv', 'r') as file:
#     data = file.readlines()
# print(data)

import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         # print(row)
#         if row[1] == 'temp':
#             continue
#         else:
#             temp = row[1]
#             temperature.append(int(temp))
# print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))
#
# data_dict =data.to_dict()
# print(data_dict)
#
# data_lis = data['temp'].to_list()
# print(data_lis)
# print(len(data_lis))
# average = sum(data_lis)/len(data_lis)
# print(average)
# temp_mean = data['temp'].max()
# print(temp_mean)
#
# print(data['condition'])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # × 9/5) + 32
# print((monday.temp[0] * 9/5) +32)
#
# data_dict = {
#     "students" : ["Amy", "james", "Angela"],
#     "score" : [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")

datas = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250627.csv')
Fur = datas['Primary Fur Color']
grey_squirrels_count = len(datas[datas["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(datas[datas["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(datas[datas["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

Data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(Data_dict)

df = pandas.DataFrame(Data_dict)
df.to_csv('new_data.csv')
# data2 = pandas.DataFrame(Fur)
#
# data2.to_csv('new_data.csv')
