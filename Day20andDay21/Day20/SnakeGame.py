import time
from turtle import Screen, Turtle

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()

    # Detect food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score(snake)

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
