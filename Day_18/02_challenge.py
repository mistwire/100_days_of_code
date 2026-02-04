# CHALLENGE 02: Draw a dashed line
# KEY CONCEPT: Toggle pen on/off to create gaps. Pattern: draw (pendown), move without drawing (penup), repeat.
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("dodger blue")
# PATTERN: Create a dashed line by toggling pen state
for _ in range(15):
    tim.forward(10)  # Draw 10 units (pendown, default)
    tim.penup()  # Stop drawing
    tim.forward(10)  # Move 10 units without drawing
    tim.pendown()  # Resume drawing for next iteration

screen = Screen()
screen.exitonclick()