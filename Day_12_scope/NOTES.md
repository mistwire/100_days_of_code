# Day 12: Scope - Global vs Local Variables & Best Practices

## What You Learned
Today you learned that variables exist in different "scopes" - global (accessible everywhere) or local (only within functions). Understanding scope is critical for writing clean, bug-free code. You also learned that while the `global` keyword can modify global variables, using **return values** is almost always better.

---

## Key Concepts

### 1. Global vs Local Scope
```python
x = 5  # GLOBAL SCOPE - defined at module level

def my_function():
    y = 10  # LOCAL SCOPE - only exists inside function
    print(x)  # Can READ global x
    print(y)  # Can READ local y

my_function()
print(x)  # Works: 5 (global still exists)
print(y)  # ERROR: NameError (local y was destroyed when function exited)
```

**Scope Rules:**
- **Global:** Defined outside all functions, exists for entire program
- **Local:** Defined inside function, created when function runs, destroyed when function exits
- **Readable:** Functions can READ global variables (but this is often not recommended)
- **Not writable (normally):** Functions create LOCAL shadows instead of modifying globals

### 2. Variable Shadowing
When local and global variables have the same name:

```python
x = "global"

def my_function():
    x = "local"  # Creates NEW local variable named x
    print(x)     # Prints "local" (reads local version)

my_function()
print(x)  # Prints "global" (global x was never touched)
```

Python searches local scope first, then global. The local variable "shadows" the global one.

### 3. The `global` Keyword (Dangerous!)
To actually modify a global variable from inside a function:

```python
counter = 0

def increment():
    global counter  # Tell Python: use the GLOBAL counter, not a local one
    counter += 1

increment()
print(counter)  # 1 (global was modified)
```

**Why it's dangerous:**
- Function has hidden side effects (modifies global state)
- Harder to test and debug
- Another function could change the global unexpectedly
- Breaks encapsulation

### 4. Return Values (Clean Alternative)
Instead of `global`, use return:

```python
counter = 0

def increment(current_count):
    """Compute and return new count (don't modify globals)."""
    return current_count + 1

counter = increment(counter)  # CALLER decides what to do with result
print(counter)  # 1
```

**Why it's better:**
- Function is predictable (no hidden side effects)
- Function can be tested independently
- Caller explicitly controls the result
- Reusable in different contexts

### 5. Constants (ALL_CAPS)
Global variables that NEVER change should be ALL_CAPS:

```python
# These are CONSTANTS - don't modify them
EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5
MAX_ATTEMPTS = 100

def set_difficulty():
    level = input("easy or hard? ")
    if level == "easy":
        return EASY_MODE_TURNS  # Using constant (safe to read)
```

Constants can be safely read from anywhere without `global` keyword.

### 6. Scope in Loops and Conditionals
Python has NO block scope (unlike Java/C/JavaScript):

```python
for i in range(5):
    x = i

print(x)  # 4 (x DOES exist outside loop!)

if True:
    y = "hello"

print(y)  # "hello" (y DOES exist outside if block!)
```

Variables created in loops/if blocks are still LOCAL to the function, but they're not destroyed when the block ends.

### 7. LEGB Rule (Scope Lookup Order)
Python searches for variables in this order:

1. **Local** - Inside current function
2. **Enclosing** - In outer function (nested functions)
3. **Global** - Module level
4. **Built-in** - Python's built-in names (print, len, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"  # Found in Local scope first
        print(x)

    inner()  # Prints "local"

outer()
```

---

## Common Pitfalls

- **Using `global` too much:** Makes code unpredictable. Use return values instead.
- **Forgetting variables die with function:** Accessing local variable outside function crashes.
- **Modifying mutable globals by accident:** Lists/dicts modified inside functions affect global (even without `global` keyword).
- **Thinking loops have scope:** Variables created in loops are still function-scope.
- **Name collisions:** Naming local variable same as global hides it (shadowing).
- **Not returning early enough:** Forgetting to use `return` leaves function running unnecessarily.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 7** | Game state (lives, display) - should be function local, not global |
| **Day 10** | Functions with return values (clean design) |
| **Day 11** | Multiple function calls, each with own local state |

---

## Before You Move On
Make sure you can:
- [ ] Explain the difference between global and local scope
- [ ] Identify what happens if you create a local variable with same name as global
- [ ] Explain why `return` is better than `global` for most cases
- [ ] Use constants (ALL_CAPS) correctly
- [ ] Trace through code to identify which scope a variable is in
- [ ] Explain why loops don't create new scope in Python

---

## Practice Prompt
**Enhancement Challenge:**
1. Rewrite the Higher/Lower game using ONLY local variables and return values (no `global` keyword)
2. Refactor to extract functions: `get_difficulty()`, `check_guess()`, `run_game_loop()`
3. Each function should have clear inputs (parameters) and outputs (return values)
4. Create a game manager function that handles the main loop

**Example Refactoring:**
```python
# BEFORE: Everything global, function modifies global state
lives = 6
score = 0

def play():
    global lives, score
    lives -= 1
    score += 10

# AFTER: Functions are pure, return new state
def play(current_lives, current_score):
    return current_lives - 1, current_score + 10

lives, score = play(lives, score)
```

**Constants Exercise:**
```python
# Define these constants at top of file
EASY_TURNS = 10
HARD_TURNS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100
WINNING_SCORE = 100

# Use them throughout the code instead of magic numbers
```

**Bonus:** Create a `game_state` dictionary to hold all game variables:
```python
game_state = {
    "number": 50,
    "guesses": 5,
    "score": 0,
    "difficulty": "hard"
}

# Pass the dict to functions
def check_guess(guess, game_state):
    # Modify game_state as needed
    game_state["guesses"] -= 1
    return game_state
```

**Bonus 2:** What's the difference between:
```python
def modify_list(lst):
    lst.append(1)  # Modifies the global list

# vs

def return_new_list(lst):
    return lst + [1]  # Returns new list, doesn't modify original
```
Which is better and why?
