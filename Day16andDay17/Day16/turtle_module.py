from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html#turtle.fd
# https://cs111.wellesley.edu/reference/colors
timmy = Turtle()

# timmy.shape("turtle")
#
# i = 8
# while i > 0:
#     timmy.color("coral")
#     timmy.fillcolor("violet")
#     timmy.begin_fill()
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.forward(100)
#     timmy.right(135)
#     timmy.forward(141.14)
#     timmy.end_fill()
#     timmy.color("green")
#     timmy.circle(72.7)
#     timmy.color("purple")
#     timmy.circle(36.35)
#     timmy.right(90)
#     i = i-1
#
#
my_screen = Screen()
print(my_screen.canvheight)


turtle = Turtle()
turtle.fillcolor("orange")
turtle.begin_fill()

for i in range(5):
    turtle.forward(150)
    turtle.left(144)

turtle.end_fill()
my_screen.exitonclick()
# from prettytable import PrettyTable
# table = PrettyTable()
#
# # table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
# # table.add_column("Type",["Electric","Water","Fire"])
# table.align = "r"
# print(table)
