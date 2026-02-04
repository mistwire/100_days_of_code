from turtle import Turtle

# KEY CONCEPT: Module-level constants make configuration easy to find and change.
# Each segment is 20x20px, so positions are spaced 20px apart.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Turtle headings use degrees: 0=East, 90=North, 180=West, 270=South.
# Named constants prevent "magic number" bugs (was 270 up or down?).
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# PATTERN: Composition over Inheritance -- Snake is NOT a Turtle.
# It *has* a list of Turtle segments. Compare with Food (Day 20), which
# inherits from Turtle because it IS a single on-screen shape.
# This distinction matters: Snake manages multiple turtles as a coordinated group.
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # Convenience reference -- head is just segments[0], but we use it constantly
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()  # prevents drawing lines as the segment moves
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # KEY CONCEPT: "Follow the Leader" algorithm.
        # Each segment moves to where the segment AHEAD of it was.
        # The loop runs BACKWARDS (tail -> neck) so we read each predecessor's
        # position BEFORE that predecessor moves. Only the head advances forward.
        # This same approach works for any "chain" movement (e.g., a train game).
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # PATTERN: Direction guards -- prevent the snake from reversing into itself.
    # A snake going UP cannot instantly go DOWN (that would be a 180-degree turn
    # through its own body). Each method checks current heading before allowing the turn.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)