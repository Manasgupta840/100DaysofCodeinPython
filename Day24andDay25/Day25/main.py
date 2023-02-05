

data = []

with open("weather_data.csv") as weater_data:
    all_data = weater_data.readlines()
    for each_day in all_data:
        data.append(each_day.strip())

# print(data[0])

import csv

with open("weather_data.csv") as weater_data:
    data = csv.reader(weater_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


