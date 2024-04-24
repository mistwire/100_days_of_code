import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed("fastest")

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_spiro(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
 
draw_spiro(5)

screen = turtle.Screen()
screen.exitonclick()
