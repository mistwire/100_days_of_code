from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("dodger blue")
for i in range(3, 10):
    tim.forward(100)
    tim.right(360/i)
    



screen = Screen()
screen.exitonclick()