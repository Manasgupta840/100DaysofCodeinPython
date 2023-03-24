import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
date = now.day
day_of_week = now.weekday()
print(f"date - {date}\nmonth - {month}\nyear - {year}  \nand day_of_week = {day_of_week}")
