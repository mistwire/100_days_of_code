#!/usr/bin/env python3

from turtle import Turtle, Screen
from pong import Paddle
from pong import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
screen.exitonclick()
