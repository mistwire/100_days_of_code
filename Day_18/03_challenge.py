from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["blue violet", "hot pink", "olive drab", "red", "blue", "orange", "black", "purple", "black", "magenta"]


def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(i)


screen = Screen()
screen.exitonclick()