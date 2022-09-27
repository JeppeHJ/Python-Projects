from turtle import Turtle

FONT = ("Courier", 24, "normal")
TEXT_POSITION = (-220, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(TEXT_POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=FONT)