# CHALLENGE 01: Draw a square
# KEY CONCEPT: Loop to draw a polygon. A square has 4 sides, each 90° turn.
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")  # Show turtle shape (triangle)
tim.color("dodger blue")
# PATTERN: Repeat 4 times to draw a closed square
# External angle = 360 / number_of_sides = 360 / 4 = 90°
for _ in range(4):
    tim.forward(100)  # Draw side
    tim.right(90)  # Turn right (external angle)

screen = Screen()
screen.exitonclick()