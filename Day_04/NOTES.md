# Day 4: Control Flow, Nested Lists & Indexing

## What You Learned

This day focuses on **nested if/elif/else statements**, **2D lists** (lists of lists), and **string indexing**. The treasure map exercise is a great example of how the same problem can be solved verbosely or concisely -- and why understanding indexing matters.

---

## Key Concepts

### 1. Nested If/Elif/Else
You can put if statements inside other if statements. Each level of nesting adds a layer of decision-making:

```python
if position[0] == "A":
    if position[1] == "1":
        line1[0] = "X"
    elif position[1] == "2":
        line2[0] = "X"
```

This works, but gets verbose fast. The treasure map has 9 possible positions and needs ~20 lines of nested conditionals.

### 2. 2D Lists (Lists of Lists)
A list can contain other lists, creating a grid:

```python
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]   # A list of 3 lists = a 3x3 grid
```

Access elements with two indices: `map[row][column]`
- `map[0]` gives you `line1` (the first row)
- `map[0][2]` gives you the third item in the first row

### 3. String Indexing
Strings work like lists -- you can access individual characters by index:

```python
position = "B2"
position[0]  # "B" -- first character
position[1]  # "2" -- second character
```

This is the same `[index]` syntax used for lists. Python uses **zero-based indexing** -- the first element is at index 0.

### 4. The `.index()` Method
```python
abc = ["a", "b", "c"]
abc.index("b")  # Returns 1 -- the position of "b" in the list
```

This converts a value into its position. Useful for mapping letters to column numbers.

### 5. Verbose vs Concise Solutions
Your solution (nested if/elif) and Angela's solution (using `.index()` and `int()`) both work. The key difference:

**Verbose (your solution)**: Explicitly handles every case. Easy to read but doesn't scale -- a 10x10 grid would need 100 branches.

**Concise (Angela's solution)**: Converts the input into indices mathematically. Scales to any grid size with the same ~4 lines of code.

```python
letter_index = abc.index(letter)        # "B" -> 1
number_index = int(position[1]) - 1     # "2" -> 1 (zero-based)
map[number_index][letter_index] = "X"   # One line handles all 9 cases
```

The lesson: when you find yourself writing repetitive if/elif blocks, there's usually a way to compute the answer instead.

---

## Common Pitfalls

- **Off-by-one errors**: Humans count from 1, Python counts from 0. The `- 1` in `int(position[1]) - 1` converts from human numbering to Python indexing.
- **Shadowing built-ins**: `map` is a built-in Python function. Using it as a variable name (`map = [line1, line2, line3]`) hides the built-in. It works, but can cause confusing bugs later.
- **Hardcoding vs computing**: If you're writing the same pattern 3+ times with slight variations, there's usually a formula or data structure that handles all cases at once.
- **Forgetting `.lower()`**: User input might be uppercase or lowercase. `position[0].lower()` normalizes it.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 2** | String indexing (`position[0]`) uses the same syntax as list indexing. Slicing (`pi_string[:52]`) extends this further |
| **Day 5** | The password generator uses lists and indexing heavily, plus `random.choice()` picks from a list by index internally |
| **Day 7** | Hangman uses string indexing to check individual letter guesses |
| **Days 20-23** | Game grids (Snake, Pong) use coordinate systems -- same concept as 2D list indexing |
| **Day 25** | Pandas DataFrames are essentially 2D data structures -- rows and columns, accessed by index or label |

---

## Before You Move On

Make sure you can:

- [ ] Create a 2D list and access a specific element with `list[row][col]`
- [ ] Use string indexing to extract individual characters
- [ ] Convert user input (like "B2") into list indices
- [ ] Explain why `int(position[1]) - 1` is needed (zero-based indexing)
- [ ] Recognize when nested if/elif can be replaced with computed indexing

---

## Practice Prompt

Build a **tic-tac-toe board display**:
- Create a 3x3 grid using a 2D list (start with all empty spaces)
- Write a function `place_mark(board, position, mark)` where position is like "A1" and mark is "X" or "O"
- Convert the position string to row/column indices (use the `.index()` approach, not nested ifs)
- Print the board after each placement
