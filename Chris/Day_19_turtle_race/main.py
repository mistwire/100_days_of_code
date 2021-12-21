import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_right():
    tim.rt(10)


def turn_left():
    tim.lt(10)


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=turn_right, key='d')
screen.onkeypress(fun=turn_left, key='a')
screen.onkeypress(fun=move_backwards, key='s')
screen.onkey(fun=turtle.resetscreen, key='c')
screen.exitonclick()
