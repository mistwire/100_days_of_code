# Day 14: Higher Lower Game -- Data Comparison, Game Flow & Dictionary Records

## What You Learned

This day combines **dictionary-based data records**, **random selection**, and a **comparison game loop** into a polished terminal game. The project ties together control flow, data structures, and module separation in a way that mirrors real-world data-driven applications.

---

## Key Concepts

### 1. Dictionary-Based Records
Each celebrity/brand is stored as a dictionary with consistent keys -- this is a lightweight version of a database record:

```python
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}
```

When every dictionary in a list has the same keys, you can treat the list like a table and each dictionary like a row. This pattern appears again in Day 25 (CSV/Pandas) where tabular data is the whole point.

### 2. Random Selection from a Data Set
```python
def get_random_data():
    contestant = random.choice(data)
    return contestant
```

`random.choice()` works on any sequence -- here it picks a random dictionary from a list of dictionaries. Compare this to Day 5 (password generator) where `random.choice()` picks from a list of characters, or Day 11 (Blackjack) where it picks from a deck. Same function, different data complexity.

### 3. The "Carry Forward" Game Loop Pattern
The clever trick in this game is how the winner persists between rounds:

```python
if players_guess == answer:
    score += 1
    first_option = second_option  # Winner carries forward
```

Instead of picking two fresh options each round, the winning option becomes the next round's "A" option. This makes the game feel continuous and gives the player a sense of building knowledge.

### 4. Comparison Logic with Conditional Assignment
```python
if first_option['follower_count'] > second_option['follower_count']:
    answer = 'a'
else:
    answer = 'b'
```

The comparison determines the correct answer before checking the player's guess. This separation of "compute the answer" from "check the guess" is a clean pattern -- it keeps the logic readable and testable.

### 5. Module Separation
The project splits into three files:
- **`game_data.py`** -- pure data (the list of dictionaries)
- **`art.py`** -- ASCII art for display
- **`main.py`** -- game logic

This separation means you could swap in different data (e.g., YouTube subscriber counts) without touching the game logic. It's the same principle behind Day 15's menu dictionary and foreshadows Day 16's class-based separation.

---

## Common Pitfalls

- **Comparing the same person to themselves**: `get_random_data()` could return the same entry twice. A production version would check `second_option != first_option` before proceeding.
- **Missing `else` for ties**: If both options have identical follower counts, the current code defaults to "b". A tie-handling branch would make the game fairer.
- **Using `os.system('clear')` for screen clearing**: This works on macOS/Linux but fails on Windows (which uses `cls`). A cross-platform approach would check `os.name`.
- **Debug output left in**: The `print(f"cheat: ...")` lines expose follower counts -- helpful for testing but should be removed for a real game.
- **`global` keyword not needed here**: The `money` pattern from Day 15 uses `global`, but Day 14 avoids it by keeping `score` in the module scope. Both work, but avoiding `global` is generally preferred.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 5** | `random.choice()` picks from a list -- same function used here on dictionaries instead of characters |
| **Day 7** | The game loop pattern (`while game_continues`) is the same structure as the Hangman game loop |
| **Day 9** | Dictionary access with bracket notation (`item['key']`) -- the core data access pattern |
| **Day 10** | Functions that return values (`get_random_data()` returns a dictionary) |
| **Day 11** | Game algorithm complexity -- Blackjack also compares values and determines winners |
| **Day 25** | Tabular data (list of dictionaries) evolves into CSV files and Pandas DataFrames |

---

## Before You Move On

Make sure you can:

- [ ] Access values in a list of dictionaries using bracket notation
- [ ] Explain why `random.choice()` works the same on a list of strings and a list of dicts
- [ ] Trace through the "carry forward" pattern and explain how `first_option` updates
- [ ] Separate a project into data, display, and logic files
- [ ] Identify the bug where both options could be the same entry

---

## Practice Prompt

Build a **"Would You Rather" quiz** using the same architecture:
- Create a `data.py` with a list of dictionaries, each containing two options and a `popularity` score for each
- Write a game loop that presents pairs and asks the player which is more popular
- Implement the "carry forward" pattern so the winner stays for the next round
- Add a check that prevents the same entry from appearing as both options
- Bonus: track and display a high score across multiple games
