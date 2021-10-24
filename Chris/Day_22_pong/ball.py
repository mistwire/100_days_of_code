import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_trajectory = 10
        self.y_trajectory = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_trajectory *= -1

    def bounce_x(self):
        self.x_trajectory *= -1
