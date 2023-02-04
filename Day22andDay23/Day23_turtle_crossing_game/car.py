from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


class Car:

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_change = random.randint(1, 10)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random_color())
            new_car.goto(180, random.randint(-140, 140))
            self.all_cars.append(new_car)

    def move_cars(self):

        for car in self.all_cars:
            car.backward(self.speed)


    def increase_speed(self):
        self.speed += MOVE_INCREMENT