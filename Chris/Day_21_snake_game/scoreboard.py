import turtle
ALIGN = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.current_score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGN, font=FONT)

    def add_point(self):
        self.current_score += 1
        self.clear()
        self.update_score()
