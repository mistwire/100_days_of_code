from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.add_segment, "a")


collision = False
while not collision:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.add_score()

    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.game_over()
            collision = True

    if snake.check_collision():
        scoreboard.game_over()
        collision = True

screen.exitonclick()
