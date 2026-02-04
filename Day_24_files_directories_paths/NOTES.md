# Day 24: Files, Directories, and Paths - Mail Merge

## What You Learned
File I/O with string templates: reading multiple files, template substitution (string.replace()), and writing dynamic outputs. This day builds on Day 2's file basics but focuses on practical automation using string manipulation and file paths.

---

## Key Concepts

### 1. File Path Handling with Relative Paths
The mail merge challenge uses relative paths to organize files:

```python
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()
```

**Key differences:**
- `./` explicitly means "current directory"
- `readlines()` returns a list with newlines included: `["Alice\n", "Bob\n"]`
- `read()` returns one string: `"Dear [name],..."`

### 2. Template-Based File Generation
The core pattern: read template → loop through data → substitute placeholders → write output

```python
for name in names:
    new_letter = letter_contents.replace("[name]", name.strip())
    # PATTERN: strip() removes the newline from readlines()
    with open(f"./Output/letter for {name}.txt", mode="w") as file:
        file.writelines(new_letter)
```

**Why this pattern?** Separates data (names) from template (letter format), making both reusable.

### 3. String Methods for Template Processing
Essential string operations for automation:

```python
# strip(): Remove whitespace/newlines from string ends
name.strip()  # "Alice\n" → "Alice"

# replace(): Substitute text patterns
letter.replace("[name]", "Alice")

# format() / f-strings: Dynamic file naming
f"./Output/letter for {name}.txt"
```

### 4. File Opening Modes
- `"r"` (read): File must exist; read-only
- `"w"` (write): Creates file or overwrites if exists
- `"a"` (append): Creates file or adds to end if exists

```python
# Read input files
with open("./Input/Names/invited_names.txt") as f:  # Default "r" mode

# Write output files (creates new file each iteration)
with open(f"./Output/letter for {name}.txt", mode="w") as f:
```

### 5. Context Managers (with statement)
The `with` statement ensures files close automatically:

```python
with open("file.txt") as f:
    data = f.read()
    # File is automatically closed here, even if error occurs
```

**Why?** Prevents resource leaks; guarantees cleanup.

---

## Common Pitfalls
- **Newlines in readlines() output**: Always call `.strip()` on names from `readlines()`
- **File not found errors**: Use `./Input/` not `Input/` for relative paths
- **Placeholder case sensitivity**: `[name]` vs `[Name]` must match exactly
- **File overwrites**: `mode="w"` overwrites existing files; use `mode="a"` to append
- **Directory structure missing**: Create `./Input/Names/`, `./Input/Letters/`, and `./Output/` directories first

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 2** | File I/O basics: reading and writing files |
| **Day 4** | String manipulation: split(), replace(), strip() |
| **Day 5** | Could use random to shuffle names or select random template |
| **Day 26** | File paths are often organized like CSV data (structured directories) |
| **Day 27-28** | Tkinter apps often read/write config files using this pattern |
| **Day 33+** | APIs return JSON/XML that uses similar template processing |

---

## Before You Move On
Make sure you can:
- [ ] Explain the difference between readlines() and read()
- [ ] Use strip() to clean up strings from readlines()
- [ ] Explain why the template pattern (read-once, use-many) is efficient
- [ ] Create nested directory structures (`./Input/Letters/`)
- [ ] Modify mail merge to read from additional template variations
- [ ] Add error handling for missing files (see Day 13: Debugging)

---

## Practice Prompt
**Challenge: Advanced Mail Merge**
1. Read multiple letter templates from `./Input/Letters/` (e.g., formal.txt, casual.txt, urgent.txt)
2. For each name, randomly select a template (Day 5 random choice)
3. Add personalization: read a second file with "preferences" (e.g., names → template_type)
4. Write output with both name AND chosen template type in filename: `letter_for_Alice_formal.txt`
5. Add a summary report: `generated_letters.txt` listing all created files

This chains file operations, randomization, and template processing into a realistic automation project.
