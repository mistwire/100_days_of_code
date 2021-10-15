from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def check_collision(self):
        if self.segments[0].xcor() > 280 or self.segments[0].xcor() < -280:
            return True
        if self.segments[0].ycor() > 280 or self.segments[0].ycor() < -280:
            return True
        else:
            return False

    def turn_up(self):
        if self.segments[0].heading() == 270:
            return
        else:
            self.segments[0].setheading(90)

    def turn_right(self):
        if self.segments[0].heading() == 180:
            return
        else:
            self.segments[0].setheading(0)

    def turn_down(self):
        if self.segments[0].heading() == 90:
            return
        else:
            self.segments[0].setheading(270)

    def turn_left(self):
        if self.segments[0].heading() == 0:
            return
        else:
            self.segments[0].setheading(180)