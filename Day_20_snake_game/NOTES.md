# Day 20: Snake Game -- Architecture and Movement

## What You Learned
You built the first half of a classic Snake game using OOP and Turtle graphics, focusing on game architecture, class-based design, keyboard controls, and collision detection with food.

---

## Key Concepts

### 1. Game Loop Pattern
The `while game_is_on` loop is the heartbeat of every game. Each tick: update the screen, pause briefly, then move objects and check for collisions.

```python
while game_is_on:
    screen.update()       # redraw everything
    time.sleep(0.1)       # control game speed (~10 FPS)
    snake.move()          # advance the snake one step
    if snake.head.distance(food) < 15:
        food.refresh()    # teleport food to a new spot
```

This is the same pattern you'll see in Day 22 (Pong) and Day 23 (Turtle Crossing). The `time.sleep()` call controls difficulty -- smaller values = faster game.

### 2. Manual Screen Refresh with `tracer(0)`
By default, Turtle draws every movement in real time, which looks janky for games. `screen.tracer(0)` disables auto-refresh, and `screen.update()` redraws everything at once -- giving you smooth animation.

### 3. Multi-Class Architecture (Separation of Concerns)
The game is split across three files, each with one job:

| File | Class | Responsibility |
|------|-------|---------------|
| `snake.py` | `Snake` | Movement, direction, segments |
| `food.py` | `Food` | Random placement on screen |
| `main.py` | *(none)* | Game loop, wiring classes together |

This is the same OOP composition pattern from Day 1 (`Car` + `Battery`), now applied to a real project.

### 4. Snake Movement -- The "Follow the Leader" Algorithm
The snake doesn't move all segments independently. Instead, each segment moves to where the segment *ahead* of it was. Only the head moves forward:

```python
def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
```

The loop runs **backwards** (from tail to second segment) so each segment reads the position of the one ahead *before* that one moves.

### 5. Direction Guards (Preventing 180-Degree Turns)
The snake can't reverse into itself. Each direction method checks the current heading before changing it:

```python
def up(self):
    if self.head.heading() != DOWN:   # can't go up if already going down
        self.head.setheading(UP)
```

### 6. Inheritance vs Composition
- **`Food`** inherits from `Turtle` (it *is* a turtle with extra behavior)
- **`Snake`** uses composition -- it *has* a list of `Turtle` segments but isn't itself a `Turtle`

This is a deliberate design choice: Food only needs one on-screen shape, while Snake manages many.

### 7. Constants as Configuration
Module-level constants like `STARTING_POSITIONS`, `MOVE_DISTANCE`, `UP`, `DOWN` make the code readable and easy to tweak without hunting through methods.

---

## Common Pitfalls
- **Forgetting `penup()`** -- without it, every turtle draws a line as it moves, leaving trails everywhere
- **Not using `tracer(0)` + `update()`** -- the game will flicker and lag without manual screen control
- **Moving segments forward instead of "following"** -- if you move each segment independently, the snake falls apart
- **Off-by-one in direction constants** -- Turtle uses degrees (0=East, 90=North, 180=West, 270=South), not compass directions
- **Collision radius too small or too large** -- `distance(food) < 15` is tuned to the 10x10 pixel food; change the food size and you'll need to adjust this

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 1** | OOP fundamentals -- classes, `__init__`, attributes, and methods are the backbone of `Snake` and `Food` |
| **Day 5** | `random.randint()` places food at random coordinates, same module used for password generation |
| **Days 18-19** | Turtle basics (shapes, movement, screen setup) that this game builds directly on |
| **Day 21** | Adds Scoreboard, wall/tail collisions, and `extend()` to complete the game |
| **Day 22** | Pong reuses this exact game loop pattern with paddles and a ball |
| **Day 12** | Scope -- `game_is_on` is a module-level variable controlling the loop from inside collision checks |

---

## Before You Move On
Make sure you can:
- [ ] Explain why `tracer(0)` and `update()` are used together
- [ ] Describe the "follow the leader" movement algorithm in your own words
- [ ] Explain why `Food` inherits from `Turtle` but `Snake` does not
- [ ] Add a new feature (like changing food color on refresh) without breaking the game loop
- [ ] Draw the class diagram: which class talks to which, and how

---

## Practice Prompt
Build a **"Tron Light Cycles"** mini-game: two snakes controlled by different keys (WASD vs arrows) that leave permanent trails. A player loses when they hit any trail. Reuse the `Snake` class but remove `penup()` so movement draws lines. You'll need two `Snake` instances and two sets of key bindings -- a preview of Day 22's two-player Pong.
