from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=80)
window.config(padx=30, pady=50)

my_label = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label.grid(row=1, column=0)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)

result_box = Label(text=0, font=("Arial", 10, "bold"))
result_box.grid(row=1, column=1)

Miles = Label(text="Miles", font=("Arial", 10, "bold"))
Miles.grid(row=0, column=2)

Km = Label(text="Km", font=("Arial", 10, "bold"))
Km.grid(row=1, column=2)


def mile_to_km():
    data = round((float(input_box.get()) * 1.60934), 2)
    result_box.config(text=data)


button = Button(text="Calculate", command=mile_to_km)
button.grid(row=2, column=1)

window.mainloop()
