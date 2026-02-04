# CHALLENGE 04: Random walk with random colors and directions
# KEY CONCEPT: Randomness combined with turtle state (heading, color, pen size).
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)  # Enable RGB color mode
tim.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turn_options = [0, 90, 180, 270]  # Four cardinal directions (East, North, West, South)
tim.pensize(15)  # Thick lines for visibility
tim.speed("fastest")  # Performance optimization

# PATTERN: Generate random RGB color tuples
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# PATTERN: Random walk loop. Each iteration:
# 1. Move forward 25 units
# 2. Change to random color
# 3. Set heading to random direction
for i in range(200):
    tim.forward(25)
    tim.color(random_color())
    # KEY CONCEPT: setheading() sets absolute direction (0=East, 90=North, 180=West, 270=South)
    # Different from right(angle) which rotates relative to current heading
    tim.setheading(random.choice(turn_options))

screen = turtle.Screen()
screen.exitonclick()

