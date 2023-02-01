import random
import turtle
from turtle import *

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
color1 = ["blue","red","cyan","purple","orange","green","yellow"]
user_input = screen.textinput(title="It's turtle race....", prompt="Choose your Difficulty level (easy/medium/hard) "
                                                                   "!! Enter a color: ").lower()

if user_input == "easy":
    i = 3
elif user_input == "medium":
    i = 5
elif user_input == "hard":
    i = 7
else:
    i = -1
    write("Please choose the correct input and try again", align="center", font=('Arial', 15, "bold"))

ordinate = 60
if i > 0:
    for i in range(i):
        tim = Turtle(shape="turtle")
        tim.color(color1[i])
        tim.penup()
        tim.goto(x=-230, y=-ordinate)
        ordinate -= 30
        all_turtles.append(tim)

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    write(f"You've won! The {winning_color} turtle is the winner!", align="center", font=('Arial', 15, "italic"))
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    write(f"You've lost! The {winning_color} turtle is the winner!", align="center", font=('Arial', 15, "italic"))
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)











screen.exitonclick()