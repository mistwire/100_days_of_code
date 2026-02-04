from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# PATTERN: Instantiate game objects with initial configuration
r_paddle = Paddle((350, 0))  # Right side at x=350
l_paddle = Paddle((-350, 0))  # Left side at x=-350
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# KEY CONCEPT: Bind different keys to each player's paddle movements
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall (top/bottom boundaries)
    # PATTERN: Check y-coordinate against screen edges (±280 from center at 300 height)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    # PATTERN: Two conditions prevent ball from getting stuck:
    #   1. distance() check: is ball close to paddle?
    #   2. xcor() check: is ball approaching from the correct direction?
    # Without xcor() check, ball could bounce mid-screen and stick to paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect right paddle miss (left player scores)
    # PATTERN: Miss detection is separate from paddle collision
    # Order matters: check paddle collision BEFORE checking miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # Detect left paddle miss (right player scores)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()