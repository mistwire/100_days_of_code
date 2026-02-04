# CHALLENGE 05: Spirograph (overlapping circles)
# KEY CONCEPT: Rotate the turtle heading before drawing circles to create spiral patterns.
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed("fastest")

# PATTERN: Generate random RGB color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# PATTERN: Draw a spirograph by rotating before each circle
def draw_spiro(size_of_gap):
    # PATTERN: Loop count derived from 360° rotation divided by gap size.
    # For gap=5, we draw 72 circles (360/5). For gap=10, we draw 36 circles.
    for i in range(int(360 / size_of_gap)):  # int() required since range() expects integer
        tim.color(random_color())
        tim.circle(100)  # Draw a circle of radius 100
        # KEY CONCEPT: Rotate heading by size_of_gap before next circle.
        # tim.heading() returns current heading; + size_of_gap rotates it.
        # setheading() sets the new heading, which changes circle orientation.
        tim.setheading(tim.heading() + size_of_gap)

# Draw spirograph with 5-degree rotations between circles
draw_spiro(5)

screen = turtle.Screen()
screen.exitonclick()
