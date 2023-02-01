import turtle as t
from turtle import Screen

import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim = t.Turtle()
screen= Screen()
screen.colormode(255)
color = ["CornflowerBlue","LightSkyBlue","WhiteSmoke","Teal","SpringGreen","DarkKhaki","Goldenrod","SandyBrown","PeachPuff","Linen","Purple"]
color1 = ["blue","red","blue","red","orange","green","pink","cyan","black","blue","red"]
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")
for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen.exitonclick()