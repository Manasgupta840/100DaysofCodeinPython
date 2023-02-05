import pandas as pd
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html
data = pd.read_csv('weather_data.csv')
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())
#Get Data in Columns
print(data.condition)

# Get Data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_tem = int(monday.temp)
print(monday_tem)


# Create a dataframe from scratch

data_dict = {
    "students" : ["Any", "james", "Angela"],
    "scores" : [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)