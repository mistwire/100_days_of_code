# CHALLENGE 03: Draw polygons (3-10 sides)
# KEY CONCEPT: Generalize polygon drawing. Each polygon has external angle = 360 / number_of_sides.
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["blue violet", "hot pink", "olive drab", "red", "blue", "orange", "black", "purple", "black", "magenta"]

# PATTERN: Generalized shape drawing function. Parameters define shape variation.
def draw_shape(number_of_sides):
    # KEY CONCEPT: External angle formula for regular polygons.
    # To close a polygon, total rotation must equal 360°.
    # Each turn: 360 / number_of_sides
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        tim.forward(100)  # Each side is 100 units
        tim.right(angle)  # Turn by calculated angle

# Loop draws triangle (3) through decagon (10), each with random color
for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)  # Draws i-sided polygon

screen = Screen()
screen.exitonclick()