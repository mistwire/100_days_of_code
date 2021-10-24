import turtle
import paddle
import time
import ball

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Machine That Goes 'Pong'")
screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball.move_ball()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # Detect collision with ceiling / floor:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect out of bounds collision
    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.goto(0, 0)
        ball.bounce_x()




screen.exitonclick()



