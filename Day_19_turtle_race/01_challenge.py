# CHALLENGE 01: Event-driven turtle control using keyboard input
# KEY CONCEPT: Higher-order functions - functions passed as arguments to other functions.

import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

# PATTERN: Control functions. Each modifies turtle state based on user input.
# These are callbacks—executed when specific keys are pressed.
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    # Clear the screen and reset turtle to starting state
    tim.clear()  # Erase all drawings
    tim.penup()  # Stop drawing
    tim.home()  # Return to origin (0, 0) and face East
    tim.pendown()  # Resume drawing

# KEY CONCEPT: Start listening for keyboard events.
# Without listen(), key events are ignored.
screen.listen()

# PATTERN: Event binding. Maps keyboard keys to function callbacks.
# CRITICAL: Pass function REFERENCE (move_forward), not function CALL (move_forward()).
# If you used move_forward(), the function would execute immediately (wrong!).
# Here, move_forward is passed as an object; screen calls it when user presses 'w'.
screen.onkey(key="w", fun=move_forward)  # W key = move forward
screen.onkey(key="s", fun=move_backward)  # S key = move backward
screen.onkey(key="a", fun=turn_left)  # A key = turn left
screen.onkey(key="d", fun=turn_right)  # D key = turn right
screen.onkey(key="c", fun=clear)  # C key = clear screen and reset

# This creates an interactive control system similar to WASD keys in games.
# Each key press triggers the corresponding function immediately.

screen.exitonclick()