from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
