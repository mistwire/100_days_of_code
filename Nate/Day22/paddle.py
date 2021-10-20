from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(paddle_cords)
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


