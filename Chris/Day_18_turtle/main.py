import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(0)
# set colormode to 0-255:
turtle.colormode(255)
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Make shapes:
shape_sides = 3
while shape_sides <= 10:
    for i in range(shape_sides):
        tim.forward(100)
        tim.right(360/shape_sides)
    shape_sides += 1
    tim.pencolor(random_color())


# Random Walk:
tim.pensize(8)

for i in range(100):
    tim.setheading(random.choice(direction))
    tim.pencolor(random_color())
    tim.forward(25)

# Spirograph:
tim.pensize(2)
for _ in range(72):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(5)

screen = turtle.Screen()
screen.exitonclick()
