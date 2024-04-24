import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turn_options = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


for i in range(200):
    tim.forward(25)
    tim.color(random_color())
    tim.setheading(random.choice(turn_options))


screen = turtle.Screen()
screen.exitonclick()

