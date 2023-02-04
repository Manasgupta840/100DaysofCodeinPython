from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fast")
        self.color("white")
        self.penup()
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, snake):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.update_scoreboard()
        if self.score % 5 == 0:
            snake.move_speed *= 0.6
