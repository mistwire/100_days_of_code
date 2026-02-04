# Day 21: Snake Game with Scoreboard

## What You Learned
File I/O and persistence: You extended the snake game from Day 20 by adding a scoreboard that tracks the player's score and displays game over. This day introduces managing game state that persists through multiple game rounds.

---

## Key Concepts

### 1. Inheritance and Extending Classes
The `Scoreboard` class inherits from `Turtle`, just like `Snake` and `Food`. This inheritance pattern allows different game objects to share common turtle functionality while having their own specialized behavior.

```python
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()  # Call parent Turtle class
        self.score = 0
        # ... configure appearance
```

### 2. Game State Management
The scoreboard tracks game state through instance variables (`self.score`) that persist across the game loop. When the game ends, this state is displayed on screen.

```python
def increase_score(self):
    self.score += 1
    self.clear()  # PATTERN: Clear old text before redrawing
    self.update_scoreboard()
```

### 3. Collision Detection
The main game loop detects three collision types: food (increase score), walls (end game), and tail (end game).

```python
# Detect collision with food
if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()  # Update game state
    snake.extend()
```

### 4. Turtle Graphics Text Management
Use `clear()` before `write()` to update text on screen without ghosting. This is crucial for dynamic UI updates.

---

## Common Pitfalls
- **Forgetting to call `clear()` before updating text** - causes overlapping text on screen
- **Collision detection tolerance too tight** - use distance() with a reasonable threshold (15-20 pixels works well)
- **Not resetting score properly** - keep track of `self.score` as an instance variable for state persistence
- **Game loop timing** - the `time.sleep(0.1)` call controls game speed; too fast is unplayable, too slow is boring

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Classes and inheritance: Scoreboard is a Turtle subclass |
| **Day 2** | File I/O foundations (not used in Day 21, but Day 24 adds file persistence) |
| **Day 20** | Core snake game mechanics (Day 21 extends this with scoreboard) |
| **Day 27** | Tkinter GUIs use similar text update patterns as Turtle graphics |

---

## Before You Move On
Make sure you can:
- [ ] Understand why Scoreboard inherits from Turtle
- [ ] Explain what `clear()` does and why it's needed before `write()`
- [ ] Trace through collision detection logic for all three scenarios
- [ ] Modify the game to save high scores to a file (preview of Day 24/Day 2)
- [ ] Adjust game speed by changing the sleep duration

---

## Practice Prompt
**Challenge: High Score Persistence**
Modify the scoreboard to:
1. Read the high score from a file at startup (use Day 2 file I/O)
2. Display both current score and high score on screen
3. If the current score beats the high score, save the new high score to the file
4. Display "NEW HIGH SCORE!" message when beaten

This bridges Day 21 (Scoreboard) with Day 2 (File I/O) and Day 24 (File operations).
