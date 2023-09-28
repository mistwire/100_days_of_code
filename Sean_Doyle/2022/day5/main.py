#!/usr/bin/env python3

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
start_position = tim.position()


def move_fowards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.setheading(tim.heading() - 10)


def move_clockwise():
    tim.setheading(tim.heading() + 10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.goto(start_position)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fowards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
