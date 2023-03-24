import random
import smtplib
import datetime as dt
import pandas
import json

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
PLACEHOLDER = "[NAME]"
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv('birthdays.csv')
new_data = data[data.day == now.day]
list = new_data[new_data.month == now.month]
print(list.items)
final_data = []
for (index, row) in list.iterrows():
    data1 = {
        "name": row['name'],
        'email': row['email']
    }

    final_data.append(data1)

print(final_data)

letter_no = random.randint(1, 3)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "Myemail@gmail.com"
password = "xhavgcokaxiikfko"
"letter_{letter_no}.txt"
with open(f"./letter_templates/letter_{letter_no}.txt") as letter_file:
    letter_content = letter_file.read()
    for element in final_data:
        stripped_name = element['name'].strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=element['email'],
                to_addrs="SenderMail@gmail.com",
                msg=f"Subject:Birthday Message\n\n{new_letter}")
