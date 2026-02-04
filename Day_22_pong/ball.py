from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # PATTERN: Store velocity as separate x/y components (classic physics simulation)
        # These change each frame to create movement and bouncing effects
        self.x_move = 10
        self.y_move = 10
        # KEY CONCEPT: ball_speed controls time.sleep() indirectly via main game loop
        # Lower speed = faster movement (less time between updates)
        self.ball_speed = 0.1

    def move(self):
        # PATTERN: Update position by adding velocity vectors
        # This is the core of physics-based movement (velocity-based, not keyframe-based)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # PATTERN: Wall bounce - reverse vertical velocity
        # Multiplying by -1 reverses direction while maintaining speed magnitude
        self.y_move *= -1

    def bounce_x(self):
        # PATTERN: Paddle bounce - reverse horizontal velocity AND increase difficulty
        self.x_move *= -1
        # KEY CONCEPT: Progressive difficulty - each paddle hit speeds up the ball
        # 0.9x means: after 10 hits, ball moves ~35% faster (0.9^10 ≈ 0.35)
        self.ball_speed *= 0.9

    def reset_position(self):
        # PATTERN: Reset state when paddle miss is detected
        self.goto(0, 0)
        self.ball_speed = 0.1  # Reset speed to initial value
        self.bounce_x()  # Start moving in random horizontal direction