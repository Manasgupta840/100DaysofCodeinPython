from turtle import Turtle, Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time
screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.setup(height=300, width=400)

player = Player()
screen.listen()
# screen.onkey(player.go_up, "Up")
screen.onkeypress(player.go_up, "Up")
score = Scoreboard()

game_is_on = True
car = Car()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    #Detect collision with car
    for current_car in car.all_cars:
        if current_car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    #Detect successfull completion
    if player.ycor() > 150:
        player.is_at_finish_line()
        car.increase_speed()
        score.increase_score()
        score.update_scoreboard()




















screen.exitonclick()