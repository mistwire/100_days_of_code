# Day 23: Turtle Crossing - Progressive Difficulty

## What You Learned
Progressive game difficulty through level scaling, random object spawning, and managing collections of game objects (cars). This day demonstrates game architecture for increasing challenge and state management across multiple difficulty levels.

---

## Key Concepts

### 1. Level-Based Difficulty Scaling
Instead of hard-coded difficulty, the game tracks level and scales challenge accordingly:

```python
class CarManager():
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE  # 5

    def level_up(self):
        # PATTERN: Incremental increase in difficulty
        self.car_speed += MOVE_INCREMENT  # +10 each level
        # Level 1: speed=5, Level 2: speed=15, Level 3: speed=25, etc.
```

This linear scaling is simple and tunable by changing constants.

### 2. Random Object Spawning
Cars are created randomly each frame, not all at once:

```python
def create_car(self):
    random_chance = random.randint(1, 6)
    if random_chance == 1:  # Only spawn 1/6 of the time
        new_car = Turtle("square")
        # ... configure car ...
        self.all_cars.append(new_car)
```

**Why random spawning?** Creates unpredictable patterns that feel more like real traffic and prevent memorizing safe paths.

### 3. Managing Collections of Objects
CarManager maintains a list of all active cars:

```python
def move_cars(self):
    for car in self.all_cars:
        car.backward(self.car_speed)
        # Each car moves independently with current level speed
```

This scales to any number of cars without changing code structure.

### 4. Win Condition and State Reset
When player reaches the finish line, level increases and player resets:

```python
# In main game loop
if player.is_at_finish_line():
    player.go_to_start()        # Reset position
    car_manager.level_up()      # Increase difficulty
    scoreboard.increase_level() # Update display
```

Note: Cars are NOT cleared (intentional design choice - old cars continue moving).

### 5. Simple Collision Detection
Uses distance and simple geometry:

```python
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
```

The `< 20` threshold accounts for both car width (40) and player size.

---

## Common Pitfalls
- **Random spawn rate feels unfair**: Adjust the `random.randint(1, 6)` range; smaller range = more cars
- **Level scaling too aggressive**: Change MOVE_INCREMENT from 10 to smaller value (5) for gentler progression
- **Collision feels inconsistent**: Ensure collision threshold (20) matches car size (40 wide)
- **Memory grows without bound**: Cars accumulate in `all_cars` list; could implement cleanup for off-screen cars
- **Player moves too slowly**: Adjust MOVE_DISTANCE in Player class (currently 10)

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Class design: Separate Player, CarManager, Scoreboard classes |
| **Day 5** | Random spawning of cars with random position and color |
| **Day 12** | Scope/globals: `all_cars` list is instance variable, not global |
| **Day 20-22** | Turtle graphics and game loop patterns |
| **Day 27** | Tkinter-based games use similar difficulty progression concept |

---

## Before You Move On
Make sure you can:
- [ ] Explain why random spawning creates better gameplay than fixed spawning
- [ ] Trace through what happens when player reaches finish line
- [ ] Modify spawn rate by changing the `random.randint()` range
- [ ] Add a speed limit (cap) so level 100 isn't impossible
- [ ] Implement cleanup: remove cars that have moved past the left edge (offscreen)

---

## Practice Prompt
**Challenge: Difficulty Curve Design**
1. Instead of linear `speed += MOVE_INCREMENT`, use exponential growth: `speed *= 1.1` each level
2. Add a "Lives" system - player gets 3 lives, loses one on collision, game over when lives=0
3. Display lives remaining on screen
4. Optional: Add powerups (larger hitbox for safety, slow-motion frame) that randomly appear
5. Track cumulative score as (level * 100 + cars_dodged)

This teaches game design balance: how do you keep difficulty interesting without being unfair?
