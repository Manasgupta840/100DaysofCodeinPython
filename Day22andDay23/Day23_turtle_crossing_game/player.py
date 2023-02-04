from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(0, -140)
    def go_up(self):
        self.forward(5)

    def is_at_finish_line(self):
        self.goto(0, -150)

