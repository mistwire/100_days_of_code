# Day 13: Debugging - Systematic Problem Solving & Error Analysis

## What You Learned
Today you learned systematic debugging techniques to find and fix errors in your code. Debugging is a critical skill - professionals spend significant time debugging. The key insight is to approach bugs methodically: describe the problem, reproduce it, trace through logic, and verify the fix.

---

## Key Concepts

### 1. Describe the Problem
Start by clearly articulating what's wrong:

```
WRONG: "My code doesn't work"
RIGHT: "The function returns 0 instead of 20, and only when the input is negative"
```

**Good descriptions include:**
- What you expected to happen
- What actually happened
- When it happens (always, sometimes, specific inputs?)
- Error message (if any)

### 2. Reproduce the Bug
Make the bug happen consistently:

```python
# DON'T: "Sometimes it crashes"
# DO: "It crashes when I call my_function(-1) with an empty list"

def test_bug():
    """Consistently reproduce the bug."""
    result = my_function(-1, [])
    print(result)  # Crashes here

test_bug()  # Run this to confirm the bug
```

Once you can reproduce it, you can experiment with fixes.

### 3. Play Computer
Trace through the code line-by-line as if you're the computer:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers("5", 3)  # What does this do?

# Play computer:
# a = "5" (string)
# b = 3 (integer)
# "5" + 3 → TypeError: can only concatenate str (not "int") to str
```

Often, playing computer reveals the bug immediately.

### 4. Print Debugging
Add print statements to see what's happening:

```python
def calculate_score(cards):
    print(f"Cards: {cards}")  # What's in the list?
    print(f"Sum: {sum(cards)}")  # Is sum correct?
    if sum(cards) == 21:
        return 0
    return sum(cards)

# Output shows what values are actually present
```

**Good print debugging:**
- Print INPUTS to functions (what did we receive?)
- Print OUTPUTS (what did we calculate?)
- Print at decision points (which branch did we take?)

### 5. Identify the Bug Location
Narrow down where the bug occurs:

```python
def buggy_program():
    # Insert prints to find the culprit
    x = calculate_something()
    print(f"After calculate: x = {x}")

    y = process_data(x)
    print(f"After process: y = {y}")

    z = final_step(y)
    print(f"After final: z = {z}")
    return z

# If z is wrong, test process_data and calculate_something separately
```

### 6. Common Bug Categories
Knowing common patterns helps you spot bugs faster:

**Off-by-one errors:**
```python
for i in range(5):
    print(i)  # 0,1,2,3,4 (NOT 1-5, NOT includes 5)

# If code assumes range(5) includes 5, bug!
```

**Type mismatches:**
```python
age = "25"  # String, not int
birthday_year = 2000 - age  # TypeError
```

**Logic errors:**
```python
if x > 10:
    print("x is big")
elif x > 5:  # Never reached if x > 10!
    print("x is medium")
```

**Mutable default arguments:**
```python
def append_to(lst=[]):  # DON'T: default is shared across calls!
    lst.append(1)
    return lst

print(append_to())  # [1]
print(append_to())  # [1, 1] - unexpected!
```

**Index errors:**
```python
lst = [1, 2, 3]
print(lst[5])  # IndexError: out of range
```

### 7. Systematic Debugging Process

1. **Describe:** What's wrong? When does it happen?
2. **Reproduce:** Make it happen consistently
3. **Play Computer:** Trace the code mentally
4. **Print Debug:** Add prints to understand flow
5. **Locate:** Find the exact line causing the bug
6. **Hypothesize:** What's the root cause?
7. **Fix:** Change code based on hypothesis
8. **Test:** Verify the fix works and doesn't break something else

### 8. Reading Error Messages
Python error messages tell you a lot:

```python
# TypeError: unsupported operand type(s) for +: 'str' and 'int'
# This tells us:
# - The error is a TypeError (type mismatch)
# - We're trying to add (the + operation)
# - Between a string and an integer (incompatible)

# IndexError: list index out of range
# This tells us:
# - We're trying to access a list with index that doesn't exist
# - Check: is the list smaller than we think? Did we calculate index wrong?

# KeyError: 'age'
# This tells us:
# - We're accessing a dictionary with a key that doesn't exist
# - The key 'age' is not in the dictionary
```

### 9. Debugging Tools
Beyond print statements:

**Python Debugger (pdb):**
```python
import pdb

def buggy_function():
    x = 5
    pdb.set_trace()  # Execution stops here, interactive debug prompt
    y = x + "10"  # You can step through line-by-line

buggy_function()
# You can:
# - Step through (n)
# - Print variables (p x)
# - Continue (c)
# - Set breakpoints (b)
```

**Testing edge cases:**
```python
# Always test:
# - Empty input []
# - Single element [1]
# - Negative numbers
# - Zero
# - Very large numbers
# - Wrong types
```

---

## Common Pitfalls

- **Not reading the full error message:** Error trace shows the EXACT line that failed
- **Assuming instead of checking:** "That variable must be 5" - print it to be sure!
- **Changing code without understanding the bug:** Random changes usually don't work
- **Not isolating the problem:** Test individual functions before blaming the whole system
- **Forgetting to remove debug prints:** Leave them commented or use a logger instead
- **Not testing the fix:** Fix the bug, but verify it doesn't break other tests
- **Ignoring warnings:** Python warnings often precede bugs

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 7** | Game loop - debug by checking game state variables |
| **Day 9** | Dictionary operations - debug by printing dict contents |
| **Day 11** | Complex logic - debug by tracing through compare() function |
| **Day 12** | Scope issues - debug by printing in different scopes |

---

## Before You Move On
Make sure you can:
- [ ] Describe a bug in clear, specific terms
- [ ] Reproduce a bug consistently
- [ ] Use print statements to trace code execution
- [ ] Trace through code manually (play computer)
- [ ] Identify common bug types (off-by-one, type error, logic error)
- [ ] Read and interpret Python error messages
- [ ] Verify that a fix works and doesn't break other code

---

## Practice Prompt
**Debugging Exercise 1: Off-by-One Errors**
```python
# BUG: This should sum numbers 1 through 10, but it's wrong
def sum_to_10():
    total = 0
    for i in range(10):
        total += i
    return total

print(sum_to_10())  # Got 45, should be 55
# Find the bug, fix it, verify it works
```

**Debugging Exercise 2: Logic Error**
```python
def check_age(age):
    if age > 18:
        return "adult"
    elif age > 13:
        return "teen"
    elif age > 5:
        return "child"
    else:
        return "toddler"

print(check_age(16))  # What does it return? Is that right?
# Test with various ages: 3, 5, 13, 16, 18, 21
```

**Debugging Exercise 3: Type Mismatch**
```python
def process_data(data):
    total = 0
    for item in data:
        total += item  # BUG: item might be a string!
    return total / len(data)

result = process_data([5, 10, "15", 20])  # Crashes here
# Fix the bug and test with mixed types
```

**Debugging Exercise 4: Trace Through Complex Logic**
```python
def calculate_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'F'
    return grade

# Trace through: calculate_grade(85)
# Write out each step like:
# score = 85
# Check: score >= 90? No
# Check: score >= 80? Yes
# grade = 'B'
# Return 'B'
```

**Debugging Exercise 5: Print Debugging**
```python
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Add print statements to debug:
# - What's the initial max_num?
# - What values does the loop see?
# - When does max_num change?
```

**Bonus Challenge: Integrate All Debugging Methods**
Take a project from earlier (Hangman, Blackjack, etc.) and:
1. Identify 3 potential bugs
2. Write test cases that would reveal each bug
3. Use print debugging to trace execution
4. Document what you found and how you'd fix it

**Bonus: Create a Bug Hunt**
```python
# Here's a program with 5 intentional bugs
def game_loop():
    score = 0
    for round in range(1, 4):  # Bug 1?
        guess = int(input("Guess: "))
        if guess == 50:  # Bug 2?
            score += 10
        else:
            score -= 1

    if score > 20:  # Bug 3?
        print("You win")

    scores = [10, 20, score]
    print(scores[3])  # Bug 4?

# Find all 5 bugs (including logic errors, not just crashes)
```
