from turtle import Screen
import time
from snake import Snake




def add_segment():
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    last_segment_cords = segments[-1].pos()
    new_segment.goto(last_segment_cords)
    segments.append(new_segment)


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.update()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")


collision = False
while not collision:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.check_collision():
        collision = True



screen.exitonclick()