from tkinter import *
from playsound import playsound
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkbox.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep:
    if reps % 2 != 0:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

    elif reps % 8 == 0:
        # If it's the 8th rep:
        # playsound('the-clock-strickes-twelve-o-clock-nature-sounds-7806.mp3')
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    else:
        # if it's 2nd/4th/6th rep:
        # playsound('clock-alarm-8761.mp3')
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 38:
        playsound('tic-tac-27828.mp3')
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        checkbox.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

checkbox = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkbox.grid(row=3, column=1)

window.mainloop()
