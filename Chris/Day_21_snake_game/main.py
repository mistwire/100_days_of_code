import turtle
import snake
import time
import food
import scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

my_snake = snake.Snake()
my_food = food.Food()
my_scoreboard = scoreboard.Scoreboard()


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

    # Detect collision with food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.add_point()

    # Detect collision with wall
    if my_snake.head.xcor() > 285 or my_snake.head.xcor() < -285 or my_snake.head.ycor() > 285 or my_snake.head.ycor() < -285:
        game_is_on = False
        my_scoreboard.game_over()

    # Detect collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            my_scoreboard.game_over()

screen.exitonclick()
