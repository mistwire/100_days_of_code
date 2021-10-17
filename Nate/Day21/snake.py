from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        snake_length = len(self.segments)
        last_segment_x = self.segments[snake_length - 1].xcor()
        last_segment_y = self.segments[snake_length - 1].ycor()
        new_segment.goto(last_segment_x, last_segment_y)
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
            print(f"{new_x}  {new_y}")
        self.head.forward(MOVE_DISTANCE)

    def check_collision(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280:
            return True
        if self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        else:
            return False

    def check_tail_collision(self):
        head_x = self.head.xcor()
        head_y = self.head.ycor()

        for seg in self.segments:
            if seg == self.head:
                pass
            elif seg.xcor() == head_x or seg.ycor() == head_y:
                return True

    def turn_up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.setheading(90)

    def turn_right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.setheading(0)

    def turn_down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.setheading(180)
