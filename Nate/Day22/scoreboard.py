from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=("currier", 24, "bold"))

    def draw_table(self):
        self.goto(0, 300)
        self.setheading(180)
        self.pensize(10)
        self.shape("square")
        for _ in range(13):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(20)

