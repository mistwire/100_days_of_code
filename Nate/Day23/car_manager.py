from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.goto(random.randrange(-280, 280, 60), random.randrange(-250, 250, 20))
        self.color(random.choice(COLORS))
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.current_move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.current_move_distance)
        if self.xcor() < -300:
            self.goto(300, random.randrange(-250, 250, 20))

    def speed_up(self):
        self.current_move_distance += MOVE_INCREMENT
