import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


screen.listen()

screen.onkey(move_forward, "space")

screen.exitonclick()
