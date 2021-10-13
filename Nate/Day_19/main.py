import colorgram
from turtle import Turtle, Screen
import random

t = Turtle()
t.speed("fastest")
t.hideturtle()
screen = Screen()
screen.colormode(255)

# colors = colorgram.extract("image.jpg", 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61),
              (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36),
              (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58),
              (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99),
              (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]
t.penup()
t.goto(-300, -300)

for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.goto(-300, t.ycor() + 50)

screen.exitonclick()
