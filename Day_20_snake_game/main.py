from turtle import Screen
import time
from snake import Snake
from food import Food

# PATTERN: Game Setup -- configure the arena before creating game objects
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Game :-)")
# KEY CONCEPT: tracer(0) disables automatic screen refresh so we control
# exactly when the screen redraws -- essential for smooth game animation.
# Without this, each turtle movement triggers a redraw and the game flickers.
# See also: Days 21-23 all use this same pattern.
screen.tracer(0) # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer

# PATTERN: Composition -- main.py wires independent classes together.
# Snake handles movement, Food handles placement. Neither knows about the other.
# This is the same design principle from Day 1 (Car + Battery).
snake = Snake()
food = Food()

# KEY CONCEPT: Event-driven input -- onkey() binds a keystroke to a method.
# The method reference is passed WITHOUT parentheses (snake.up, not snake.up()).
# Parentheses would call it immediately; without them, it's called when the key is pressed.
screen.listen() # listen for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# PATTERN: Game Loop -- the core of every game. Each iteration is one "frame."
# This same structure appears in Day 21, Day 22 (Pong), and Day 23 (Turtle Crossing).
game_is_on = True

while game_is_on:
    screen.update()    # manually redraw the screen (paired with tracer(0) above)
    time.sleep(0.1)    # ~10 FPS -- controls game speed; smaller = faster
    snake.move()
    # Detect collision with food
    # KEY CONCEPT: distance() returns pixel distance between two turtles.
    # 15px threshold accounts for the size of both the snake head and the food.
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
