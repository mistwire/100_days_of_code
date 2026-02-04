# Day 22: Pong - Two-Player Game

## What You Learned
Two-player game mechanics, physics simulation (ball bouncing), and coordinate-based collision detection. This day teaches scaling mechanics (ball speed increases) and complex conditional logic for game state management.

---

## Key Concepts

### 1. Object-Oriented Game Architecture
Each game component is a separate class with specific responsibilities:

```python
# Paddle: Handles player input and position
class Paddle(Turtle):
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

# Ball: Manages position, velocity, and physics
class Ball(Turtle):
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
```

### 2. Physics Simulation: Velocity and Bouncing
Instead of moving to fixed positions, the ball has velocity properties (`x_move`, `y_move`) that update each frame. Bouncing reverses velocity:

```python
def bounce_y(self):
    # WALL BOUNCE: Reverse vertical direction
    self.y_move *= -1

def bounce_x(self):
    # PADDLE BOUNCE: Reverse horizontal direction AND increase speed
    self.x_move *= -1
    self.ball_speed *= 0.9  # PATTERN: Each bounce makes game faster
```

**Why multiply by -1?** It changes direction while maintaining speed. This is fundamental to physics simulation.

### 3. Collision Detection with Distance
Use the Turtle `distance()` method to check if two objects are close enough to collide:

```python
# PATTERN: Two separate conditions to handle left and right paddles
if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
    ball.bounce_x()
elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
```

The `xcor()` check prevents double-bouncing when the ball is at the edge.

### 4. Two-Player Input Handling
Different players use different keys; the screen's `onkey()` method can bind multiple functions:

```python
screen.onkey(r_paddle.go_up, "Up")      # Right player: arrow keys
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")       # Left player: w/s keys
screen.onkey(l_paddle.go_down, "s")
```

### 5. Score Tracking and Reset
When a paddle misses, the opposing player scores and the ball resets:

```python
if ball.xcor() > 380:
    # Right paddle missed, left player scores
    ball.reset_position()
    scoreboard.l_point()

def reset_position(self):
    self.goto(0, 0)
    self.ball_speed = 0.1
    self.bounce_x()  # Start moving toward a random paddle
```

---

## Common Pitfalls
- **Ball passes through paddle**: Collision threshold too small; use 50 pixels for paddle width
- **Ball gets stuck**: Add the `xcor()` check to avoid double-bouncing at boundaries
- **Ball moves too fast immediately**: Initialize `ball_speed` and only increment after paddle hits
- **Paddles move off screen**: No boundary checking; consider adding min/max y-coordinate limits
- **Score increments twice**: Miss detection is separate from paddle collision; order matters

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Class design: Each component (Paddle, Ball, Scoreboard) is a separate class |
| **Day 5** | Random number generation (could randomize ball direction on reset) |
| **Day 12** | Global variables: `game_is_on` controls the main loop |
| **Day 20-21** | Turtle graphics and screen management |
| **Day 27** | Similar architecture will scale to Tkinter with canvas-based games |

---

## Before You Move On
Make sure you can:
- [ ] Explain why multiplying velocity by -1 creates a bounce effect
- [ ] Trace through the ball's path when it hits a paddle
- [ ] Understand why `ball_speed *= 0.9` makes the game progressively harder
- [ ] Identify all three collision detection scenarios (wall, paddles, miss)
- [ ] Modify the game to add a maximum paddle speed (prevents cheating with rapid key presses)

---

## Practice Prompt
**Challenge: Add Difficulty Levels**
1. Start ball at a fixed slow speed
2. After each successful paddle hit, increase `ball_speed` by 0.95x (multiply by 0.95)
3. Add a difficulty indicator on screen that increases with each rally
4. Reset everything when a player scores (current behavior)
5. Optional: Add paddle-position-based spin (if ball hits top of paddle, angle up more)

This reinforces physics simulation and state management concepts.
