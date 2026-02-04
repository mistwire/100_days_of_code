from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        # KEY CONCEPT: Paddles are Turtle objects positioned by constructor argument
        # This allows left and right paddles to share same class with different positions
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Tall and thin paddle shape
        self.penup()
        self.goto(coordinates)  # PATTERN: Use constructor parameter for initialization
        self.showturtle()

    def go_up(self):
        # PATTERN: Calculate new position, only change Y coordinate
        # Keep X fixed (paddle moves vertically only)
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        # NOTE: No boundary checking here - paddles can move off screen!
        # See Day 22 practice prompt to add this feature

