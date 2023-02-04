from turtle import Turtle, Screen
import random
tim = Turtle()
# ________________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________
# _______Square_________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________________________________________________________________

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# tim.left(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# tim.right(134)
# for _ in range(10):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")
color = ["blue","red","blue","red","orange","green","pink","cyan","black","blue","red"]
i = 3
screen = Screen()
tim.speed("fastest")
screen.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
tim.left(180)
tim.color("white")
tim.forward(600)
tim.right(90)
while i < 11:
    tim.color(random_color())
    for _ in range(i):
        tim.forward(100)
        tim.right((360/i))

    i += 1



screen.exitonclick()