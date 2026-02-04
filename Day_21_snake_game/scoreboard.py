from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    # KEY CONCEPT: Inherits from Turtle to reuse graphics capabilities
    # See Day 1 for class inheritance basics

    def __init__(self) -> None:
        super().__init__()  # Initialize parent Turtle class
        # PATTERN: Instance variable for persistent state across game loop
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()  # Hide the turtle cursor, only show text
        self.update_scoreboard()


    def update_scoreboard(self):
        # PATTERN: Always clear() before write() to prevent text ghosting
        # This is crucial for dynamic UI updates in Turtle graphics
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # KEY CONCEPT: clear() erases all turtle drawings at current position
        # Without this, old score text would overlap with new text
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        # Display final game state without clearing (intentional design choice)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)