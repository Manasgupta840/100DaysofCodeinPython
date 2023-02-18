from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
import json

import math


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def searchPassword():
    website = website_text.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            jsonData = data[website]
            messagebox.showinfo(title="Your information",
                                message=f"email : {jsonData['email']}\npassword: {jsonData['password']}")
        else:
            messagebox.showerror(title=f"Error in fetching details of {website}",
                                 message=f"There is no data available of {website} You can make a new password for it!!!")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    new_data = {
        website:{
            "email":email,
            "password":password,
        },
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="OOps", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:

                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=password_image)
# timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=1)

website_lable = Label(text="Website:", bg="white")
website_lable.grid(row=1, column=0)

website_text = Entry(width=32)
website_text.focus()
website_text.grid(row=1, column=1)

search_btn = Button(text="Search", width=14, highlightcolor='blue', command=searchPassword)
search_btn.grid(row=1, column=2)

email_lable = Label(text="Email/Username:", bg="white")
email_lable.grid(row=2, column=0)
email_text = Entry(width=50)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, 'manasgupta@gmail.com')

password_lable = Label(text="Password:", bg="white")
password_lable.grid(row=3, column=0)

password_text = Entry(width=32)
password_text.grid(row=3, column=1)
generate_password = Button(text="Generate Password", bg="white", command=generate_password)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=43, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
