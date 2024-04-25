# Learning higher order functions
import turtle 

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    tim.forward(50)

screen.listen()

# Functions as inputs
screen.onkey(key="space", fun=move_forward)

screen.exitonclick() 

