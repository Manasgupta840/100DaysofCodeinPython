from turtle import  Screen,Turtle

tim = Turtle()
john = Turtle()
peter = Turtle()

screen = Screen()

#shape
tim.shape("turtle")
tim.shapesize(2)

john.shapesize(2)
john.shape("turtle")

peter.shapesize(2)
peter.shape("turtle")


#Color
tim.color("CornflowerBlue")
john.color("SpringGreen")
peter.color("red")

tim.forward(10)
john.forward(20)
screen.exitonclick()
