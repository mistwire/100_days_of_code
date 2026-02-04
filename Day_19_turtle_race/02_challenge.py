# CHALLENGE 02: Turtle race with user betting and random movement
# KEY CONCEPT: Manage multiple objects (6 racing turtles) with independent state.
# Demonstrates: user input dialog, game loop, collision detection (finish line check), and randomness.

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)  # Set screen size: 500 wide, 400 tall

# PATTERN: User input via dialog. Returns the color name they bet on (or None if cancelled).
user_bets = screen.textinput(title="Make Your Bets!", prompt="Which turtle color will win the race?")

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
starting_y_positions = [-70, -40, -10, 20, 50, 80]  # Y positions for each turtle
race_running = False
all_turtles = []

# PATTERN: Create multiple objects in a loop and store in a list.
# Each turtle is independent with its own color and Y position.
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()  # Don't draw lines (racing, not painting)
    # Starting position: left side (X = -230) at assigned Y position
    new_turtle.goto(-230, starting_y_positions[turtle_index])
    all_turtles.append(new_turtle)  # Add to list for later access

# PATTERN: Conditional game start. Only race if user entered a bet.
if user_bets:
    race_running = True

# PATTERN: Main game loop. Continues until a turtle crosses the finish line.
while race_running:
    # Iterate through all turtles each frame
    for turtle in all_turtles:
        # KEY CONCEPT: Win condition. First turtle to reach X >= 230 (right side) wins.
        # xcor() returns the X coordinate of the turtle.
        if turtle.xcor() >= 230:
            race_running = False  # Exit loop immediately
            winning_color = turtle.pencolor()  # Get winner's color
            # Check user's bet against winner
            if winning_color == user_bets:
                print(f"You've won! The {winning_color} turtle has won!")
            else:
                print(f"You've lost! The {winning_color} turtle has won!")

        # PATTERN: Random movement. Each turtle advances randomly per iteration.
        # 0-10 units of movement creates unpredictability.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()