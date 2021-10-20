# TODO Scoreboard class
# TODO The ping pong ball class
# TODO paddle class
# TODO board class , could be part of the scoreboard class

from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.mode("logo")
game_on = True


scoreboard = Scoreboard()
# scoreboard.draw_table()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()


while game_on:
    time.sleep(0.1)
    ball.move()
    scoreboard.update_scoreboard()
    screen.update()

    if ball.hit_wall():
        if ball.xcor() > 1:
            scoreboard.l_score += 1
        else:
            scoreboard.r_score += 1
        ball.reset_position()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # if ball.hit_wall():
    #     if ball.direction == "right":
    #         scoreboard.l_score += 1
    #         game_on = False
    #
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
    #     ball.bounce_limiter = True
    #     ball.bounce()


screen.exitonclick()
