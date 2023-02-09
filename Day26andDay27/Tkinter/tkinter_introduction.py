import random
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# We cannot use grid or pack at the same time
# my_label.grid(column=0, row=0)
my_label.pack()
my_label.place(x=0, y=0)
# my_label["text"] = "New Text"
# my_label.config(text="Hello")
text = ["My", "name", "Hello"]


def button_clicked():
    data = input.get()
    my_label.config(text=f"{data}")


input = Entry(width=10)
input.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry



window.mainloop()
