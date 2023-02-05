import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df = pd.DataFrame(data.groupby(['Primary Fur Color'])['Primary Fur Color'].size().reset_index(name='counts'))
df.to_csv("squirrel_primary_Fur colour count")
