#!/usr/bin/env python3

import colorgram
import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.hideturtle()

# number of rows and columns
rows = 10
columns = 10
screen.setup(width=columns * 40, height=rows * 40)
screen.setworldcoordinates(-1, -1, columns * 2.5, rows * 2.5)

colors = [
    (245, 243, 237),
    (248, 241, 244),
    (238, 240, 246),
    (201, 164, 112),
    (239, 246, 241),
    (152, 75, 50),
]

for i in range(rows):
    if i % 2 == 0:
        tim.setheading(0)
    else:
        tim.setheading(180)
    for _ in range(columns):
        tim.pendown()
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(2)
    tim.setheading(90)
    tim.forward(2)
screen.exitonclick()
