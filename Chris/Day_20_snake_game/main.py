import turtle
import snake
import time

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

my_snake = snake.Snake()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()


screen.exitonclick()
