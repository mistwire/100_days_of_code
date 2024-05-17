from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Game :-)")
screen.tracer(0) # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer 

snake = Snake()
food = Food()

screen.listen() # listen for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
