from turtle import Turtle
import random  # Same random module from Day 5 (password generator)

# PATTERN: Inheritance -- Food IS a Turtle (single on-screen shape).
# Compare with Snake (Day 20), which uses composition (HAS turtles).
# Inheriting from Turtle gives Food all positioning/display methods for free.
class Food(Turtle):
    def __init__(self):
        super().__init__()  # Day 1 concept: always call parent's __init__
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # half-size = 10x10px
        self.color("purple")
        self.speed("fastest")  # no animation delay when teleporting
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        """Teleport to a new random position within the game boundaries.
        Called from main.py whenever the snake eats the food."""
        # -280 to 280 keeps food inside the 600x600 screen (origin at center)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
