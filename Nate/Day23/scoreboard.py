from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Level: {self.level}", align="center", font=("currier", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("currier", 24, "bold"))
