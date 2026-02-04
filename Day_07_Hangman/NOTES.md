# Day 7: Hangman Game - Custom Modules & Game Loops

## What You Learned
Today you built a complete text-based Hangman game, learning how to organize code into custom modules and implement a game loop with multiple win/loss conditions. This teaches the importance of breaking code into reusable pieces and managing game state.

---

## Key Concepts

### 1. Custom Modules (Imports)
Python allows you to split code into separate `.py` files and import them. In this project:
- `hangman_art.py` contains ASCII art (logo and stages)
- `hangman_words.py` contains the word list
- `main.py` imports both and uses their data

```python
import hangman_art
import hangman_words
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
```

**Why this matters:** Large projects can't live in one file. Modules organize code by responsibility.

### 2. random.choice() for Game Variety
Picks one random element from a list each game:
```python
chosen_word = random.choice(hangman_words.word_list)  # Different word every game
```

### 3. List Mutation in Game State
The `display` list changes during gameplay - it's mutable:
```python
display = ['_', '_', '_', '_']  # Start with blanks
# When player guesses 'A' in "APPLE":
display[0] = 'A'  # Now: ['A', '_', '_', '_']
```

### 4. Game Loop with Multiple Conditions
The game has two exit points:
- **Win condition:** All underscores revealed (`"_" not in display`)
- **Loss condition:** Lives reach zero (`lives == 0`)

```python
while not end_of_game:
    # Game logic...
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You lose.")
```

### 5. Tracking State with Multiple Variables
Games need to remember several things:
- `chosen_word` - the secret
- `guessed_letters` - prevent re-guessing
- `lives` - countdown mechanic
- `display` - visible progress
- `end_of_game` - exit condition

### 6. Comparing User Input Against Hidden Data
The core loop compares user's guess position-by-position:
```python
for position in range(word_length):
    if chosen_word[position] == guess:
        display[position] = letter  # Reveal it
```

This is more efficient than checking `if guess in chosen_word` multiple times.

---

## Common Pitfalls

- **Forgetting to track guessed letters:** Players can spam the same wrong guess without penalty. Use a list to prevent this.
- **Wrong indexing logic:** Make sure `display` always has the same length as `chosen_word`.
- **Not updating lives correctly:** Deduct lives only for wrong guesses, not repeated ones.
- **Exit condition issues:** Check both win AND loss conditions each loop iteration.
- **ASCII art not displaying:** Verify the import path matches the filename exactly (case-sensitive on some systems).
- **Can't find imported modules:** Keep all `.py` files in the same folder or adjust `sys.path`.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 4** | `range()` and `for` loops iterate through word positions |
| **Day 5** | `random.choice()` picks a word from a list |
| **Day 6** | Functions organize code (not used here yet, but good refactoring) |
| **Day 14+** | Higher/Lower game uses similar game loop and state tracking |
| **Day 20-23** | Turtle games use game loops with multiple conditions |

---

## Before You Move On
Make sure you can:
- [ ] Explain why we split code into `hangman_art.py` and `hangman_words.py`
- [ ] Trace through the game: what happens when a player guesses a correct letter?
- [ ] Modify the word list or add new ASCII art stages
- [ ] Explain why we use `guessed_letters` list instead of just checking the word
- [ ] Write a similar game loop for a different project

---

## Practice Prompt
**Enhancement Challenge:**
Modify the game to:
1. Track and display the number of incorrect guesses vs total guesses
2. Add a difficulty level that changes lives (easy=10, hard=3)
3. Prevent the player from guessing non-alphabetic characters
4. Add a hint system that reveals one letter after 3 wrong guesses

**Bonus:** Create a new custom module called `hangman_hints.py` that contains hints for each word, and import it into main.
