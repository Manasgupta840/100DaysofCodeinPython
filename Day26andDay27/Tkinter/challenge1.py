import random
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=50)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# We cannot use grid or pack at the same time
my_label.grid(column=0, row=0)
# my_label["text"] = "New Text"
# my_label.config(text="Hello")
text = ["My", "name", "Hello"]


def button_clicked():
    data = input.get()
    my_label.config(text=f"{data}")


input = Entry(width=10)
input.grid(column=3, row=2)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

# Entry



window.mainloop()
