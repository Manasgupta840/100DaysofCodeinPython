from turtle import Turtle, Screen
from Day22andDay23.Day22_ping_pong_game.paddle import Paddle
from Day22andDay23.Day22_ping_pong_game.ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

# setup Screen
screen.setup(height=600, width=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")
divider = Turtle()
divider.color("white")
divider.hideturtle()
divider.penup()
divider.goto(0, 300)
divider.right(90)
divider.pensize(2)

for _ in range(30):
    divider.pendown()
    divider.forward(10)
    divider.penup()
    divider.forward(10)

left_paddle = Paddle(-380, 0)
right_paddle = Paddle(380, 0)

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
print(ball.heading())
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with  r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect ball is missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
