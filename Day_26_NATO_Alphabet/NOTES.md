# Day 26: NATO Alphabet - List and Dictionary Comprehensions

## What You Learned
Advanced data structure creation using comprehensions: building lists and dictionaries from existing data in single expressions. This day demonstrates Pythonic, readable ways to transform data compared to traditional loops.

---

## Key Concepts

### 1. List Comprehensions - Condensed for Loops
Create new list from existing list in a single expression:

```python
# Traditional for loop (verbose)
squared_numbers = []
for x in numbers:
    squared_numbers.append(x * x)

# List comprehension (concise)
squared_numbers = [x * x for x in numbers]

# With filtering (conditional)
even_numbers = [x for x in numbers if x % 2 == 0]
```

**Pattern:** `[expression for item in iterable if condition]`

### 2. Dictionary Comprehensions - Mapping Keys to Values
Create dictionaries by transforming another collection:

```python
# Convert list to word-length mapping
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {k: len(k) for k in sentence.split()}
# Output: {"What": 4, "is": 2, "the": 3, ...}

# Transform existing dict values
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15}
weather_f = {k: ((v * 9/5) + 32) for k, v in weather_c.items()}

# Filter dict while transforming
scores = {"Alice": 85, "Bob": 62, "Carol": 91}
passed = {k: v for k, v in scores.items() if v >= 60}
```

**Pattern:** `{key_expr: value_expr for item in iterable if condition}`

### 3. CSV to Dictionary - Practical Application
Convert CSV data to dictionary using comprehension:

```python
import pandas

df = pandas.read_csv("nato_alphabet.csv")
# DataFrame has columns: 'letter', 'code' (A->Alfa, B->Bravo, etc.)

# Dict comprehension using iterrows()
nato_dict = {row.letter: row.code for index, row in df.iterrows()}

# Result: {"A": "Alfa", "B": "Bravo", "C": "Charlie", ...}
```

This is more efficient than manual loops, especially for large datasets.

### 4. Iterating DataFrames with iterrows()
Loop through DataFrame rows, accessing values by column name:

```python
student_df = pandas.DataFrame({
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
})

# iterrows() returns (index, row) tuples
for (index, row) in student_df.iterrows():
    print(index)          # 0, 1, 2
    print(row.student)    # Angela, James, Lily
    print(row.score)      # 56, 76, 98
```

**Pattern:** Use for converting DataFrames to dicts or processing rows conditionally.

### 5. Nested Comprehensions (Advanced)
Create complex data structures combining comprehensions:

```python
# List of lists from matrix
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in matrix for x in row]  # [1, 2, 3, 4, 5, 6]

# Dict from two lists
names = ["Alice", "Bob", "Carol"]
ages = [25, 30, 28]
people = {name: age for name, age in zip(names, ages)}
```

---

## Common Pitfalls
- **Syntax confusion**: Remember `if` is at END: `[x for x in list if condition]`, not `[x if condition for x in list]`
- **Dict comprehension value errors**: Make sure value expression is valid; watch for type mismatches
- **iterrows() performance**: Slow on large DataFrames; use `.apply()` for better performance
- **Forgetting to reference column names**: In iterrows(), use `row.column` not just `row`
- **Comprehension readability**: If it gets too complex, use traditional loops instead

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Classes and objects; comprehensions work with any iterable |
| **Day 4** | String operations: split(), join() used in comprehensions |
| **Day 5** | Random selection with `random.choice()` in comprehensions |
| **Day 8** | Loop patterns; comprehensions are optimized loops |
| **Day 25** | DataFrames and iterrows(); comprehensions transform data |
| **Day 27-28** | Tkinter: create widget lists with comprehensions |
| **Day 33+** | JSON data transformation uses similar comprehension patterns |

---

## Before You Move On
Make sure you can:
- [ ] Write list comprehension with filtering: `[x for x in list if condition]`
- [ ] Write dictionary comprehension: `{key: value for k, v in items()}`
- [ ] Use iterrows() to convert DataFrame to dictionary
- [ ] Explain why comprehensions are faster than loops
- [ ] Identify when comprehensions make code less readable (and use loops instead)
- [ ] Nest comprehensions correctly: `[x for row in matrix for x in row]`

---

## Practice Prompt
**Challenge: Data Transformation Pipeline**
1. Read NATO alphabet CSV into DataFrame
2. Create dict with comprehension (A→Alfa, etc.)
3. Read a second CSV with common words
4. Filter words to only 3-5 letters using comprehension
5. Create word→NATO_phonetics mapping with nested comprehension
6. Example output: {"cat": ["Charlie", "Alfa", "Tango"]}
7. Save result to JSON (Day 33 preview)
8. Optional: Create command-line tool that takes word input, outputs phonetics

This chains Days 24 (file I/O), 25 (pandas), 26 (comprehensions) into realistic data pipeline.
