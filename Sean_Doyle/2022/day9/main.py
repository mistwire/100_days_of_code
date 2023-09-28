#!/usr/bin/env python3

from turtle import Turtle, Screen
from pong import Paddle
from pong import Scoreboard
from pong import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
SLEEP_TIME = 0.05
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score > 3 or score.r_score > 3:
        score.game_over()
        game_is_on = False

screen.exitonclick()
