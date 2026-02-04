# Day 2: File Handling & Exception Handling

## What You Learned

This day covers how Python reads and writes files, handles errors gracefully, and stores data persistently using JSON. These are essential skills -- almost every real application needs to read files, handle unexpected input, or save state between runs.

---

## Key Concepts

### 1. Reading Files with `pathlib.Path`
`pathlib` is Python's modern way to work with file paths. It replaces older approaches like `open()` for simple operations.

```python
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()          # Read entire file as a string
lines = contents.splitlines()        # Split into a list of lines
```

- `Path` is a class (OOP from Day 1!) -- `path.read_text()` is calling a method on an object
- `read_text()` reads the whole file at once -- fine for small/medium files
- `splitlines()` is cleaner than splitting on `\n` because it handles different line endings

### 2. Writing Files
```python
path = Path('programming.txt')
path.write_text(contents)            # Overwrites the entire file
```

- `write_text()` replaces the file's contents entirely -- it doesn't append
- Build your full string first (with `+=`), then write once

### 3. Exception Handling: try/except/else
The `try/except/else` pattern is Python's way of handling errors without crashing:

```python
try:
    contents = path.read_text()       # Code that might fail
except FileNotFoundError:             # What to do if it fails
    print("File not found")
else:
    words = contents.split()          # Only runs if try succeeded
```

The three blocks:
- **try**: Code that might raise an error
- **except**: Catches a specific error type and handles it
- **else**: Runs only if no error occurred -- keeps the "happy path" separate from error handling

### 4. JSON for Data Persistence
JSON lets you save Python data structures (lists, dicts, strings, numbers) to files and load them back:

```python
import json

json.dumps(data)    # Python object -> JSON string ("dump string")
json.loads(string)  # JSON string -> Python object ("load string")
```

- `dumps` = dump to **s**tring (not to a file)
- `loads` = load from **s**tring (not from a file)
- JSON only handles basic types: strings, numbers, lists, dicts, booleans, None

### 5. Function Decomposition
`remember_me.py` demonstrates breaking a program into focused functions:
- `get_stored_username()` -- handles file reading
- `get_new_username()` -- handles user input and saving
- `greet_user()` -- orchestrates the flow

Each function does one thing. This makes code easier to test, debug, and reuse.

---

## File-by-File Summary

| File | What It Demonstrates |
|------|---------------------|
| `file_reader.py` | Reading a file, `splitlines()`, looping over lines |
| `pi_string.py` | Building a string from file lines, `lstrip()`, `in` operator for substring search |
| `word_count.py` | `try/except/else`, `split()` for word counting, looping over multiple files |
| `division_calculator.py` | `try/except/else` with `ZeroDivisionError`, `while True` loop with `break` |
| `write_message.py` | Writing to files with `write_text()`, string concatenation with `+=` |
| `number_writer.py` | Saving a Python list to JSON with `json.dumps()` |
| `number_reader.py` | Loading data back from JSON with `json.loads()` |
| `remember_me.py` | Full pattern: check if file exists, load or create data, function decomposition |

---

## Common Pitfalls

- **Catching too broadly**: `except Exception` catches everything and hides real bugs. Always catch specific errors like `FileNotFoundError` or `ZeroDivisionError`.
- **Forgetting encoding**: `read_text(encoding='utf-8')` is safer for files with special characters (as done in `word_count.py`).
- **`write_text()` overwrites**: If the file already exists, `write_text()` replaces it entirely. There's no built-in "append" on Path -- for appending, you'd use `open(path, 'a')`.
- **JSON vs Python**: JSON uses `null` (not `None`), `true`/`false` (not `True`/`False`), and doesn't support tuples or sets.
- **`path.exists()` race condition**: Between checking `path.exists()` and reading the file, the file could be deleted. The `try/except` approach in `word_count.py` is actually more robust than the `if path.exists()` approach in `remember_me.py`.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 1** | `Path` is a class -- `path.read_text()` is calling a method on an instance, just like `my_car.read_odometer()` |
| **Day 6** | You'll use `pytest` to write tests. Exception handling helps you test edge cases |
| **Day 9** | Dictionaries (which you save/load with JSON) become central to data handling |
| **Day 24** | File paths and directories are expanded -- mail merge project reads templates and writes personalized letters |
| **Day 25** | Pandas `read_csv()` replaces manual file parsing for structured data |
| **Days 33-40** | API responses are JSON -- `json.loads()` is how you parse them. Same concept, different source |

---

## Before You Move On

Make sure you can:

- [ ] Read a text file and process it line-by-line using `pathlib.Path`
- [ ] Write a `try/except/else` block and explain when each block runs
- [ ] Save a Python dictionary to a JSON file and load it back
- [ ] Explain the difference between `json.dumps()` and `json.loads()`
- [ ] Break a multi-step program into focused functions (like `remember_me.py`)

---

## Practice Prompt

Build a simple **contact book**:
- Store contacts as a list of dictionaries in a JSON file
- Functions: `add_contact(name, phone)`, `find_contact(name)`, `list_contacts()`
- Handle the case where the JSON file doesn't exist yet (first run)
- Handle invalid input gracefully with try/except
