from turtle import Turtle, Screen
from random import randint
from random import choice

tom = Turtle()
tom.shape("arrow")
tom.color("orange")
tom.speed("fastest")
screen = Screen()
screen.colormode(255)


# def draw_shape(sides):
#     for _ in range(i):
#         tom.forward(100)
#         angle = 360 / i
#         tom.right(angle)
#     tom.home()


def random_color(turtle_object):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tom.pencolor(r, g, b)


angle = 0

for _ in range(0, 2):
    while angle < 360:
        random_color(tom)
        tom.setheading(angle)
        tom.circle(100)
        angle += 5
    tom.setheading(0)
    tom.forward(100)
    angle = 0

screen.exitonclick()
