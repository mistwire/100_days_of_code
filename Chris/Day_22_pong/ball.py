import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_trajectory = 10
        self.y_trajectory = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_trajectory *= -1

    def bounce_x(self):
        self.x_trajectory *= -1
        # Increase speed of ball after each bounce:
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # Reset ball speed after point
        self.move_speed = 0.1
        self.bounce_x()
