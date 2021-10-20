from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dist = 10
        self.y_dist = 10
        #self.bounce_limiter = True
        #self.setheading(20)
        #self.direction = "right"

    def move(self):
        move_x = self.xcor() + self.x_dist
        move_y = self.ycor() + self.y_dist
        self.goto((move_x, move_y))

        if self.ycor() > 280 or self.ycor() < -280:
            self.y_bounce()
        # self.forward(10)
        # if self.ycor() > 290 or self.ycor() < -290:
        #     if self.bounce_limiter:
        #         self.bounce()
        #         self.bounce_limiter = False

    # def bounce(self):
    #     if self.direction == "right":
    #         if self.heading() < 90:
    #             new_heading = self.heading() + 90
    #             self.setheading(new_heading)
    #         else:
    #             new_heading = self.heading() - 90
    #             self.setheading(new_heading)

    def x_bounce(self):
        self.x_dist *= -1

    def y_bounce(self):
        self.y_dist *= -1

    def hit_wall(self):
        if self.xcor() > 380 or self.xcor() < -380:
            return True

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
