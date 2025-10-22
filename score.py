from turtle import Turtle
with open("data.txt") as file:
    HIGH = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score:{self.score} Highscore:{self.high_score}", align="center", font=("ariel", 20, "normal"))

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as fl:
                fl.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.high_score}", align="center", font=("ariel", 20, "normal"))

    def score_update(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score:{self.score} Highscore: {self.high_score}", align="center", font=("ariel", 20, "normal"))
