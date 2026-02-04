# Day 10: Functions with Return Values - Calculator & Modular Design

## What You Learned
Today you learned that functions are more powerful when they **return values**. Instead of just printing results, functions can compute something and hand data back to the caller. This enables function chaining, data transformation, and reusable logic. You also used dictionaries to store function references, creating a lookup table for operations.

---

## Key Concepts

### 1. Return Values vs Printing
There's a big difference:

```python
# VERSION 1: Prints but doesn't return (dead end)
def add_print(n1, n2):
    print(n1 + n2)  # Can't use this result anywhere else

result = add_print(5, 3)  # result = None
print(result)  # None (nothing to work with)

# VERSION 2: Returns (caller controls output)
def add_return(n1, n2):
    return n1 + n2  # Caller gets the value

result = add_return(5, 3)  # result = 8
print(result)  # 8 (we can do whatever we want with it)
answer = result * 2  # 16 (we can use it in calculations)
```

**Why it matters:** Returning allows the caller to decide what to do with the result.

### 2. Using Returned Values in Chains
```python
# Calculator chain multiple operations
num1 = 10
num2 = 5

answer1 = add(num1, num2)      # answer1 = 15
answer2 = multiply(answer1, 2) # answer2 = 30 (uses previous result)
print(answer2)                  # 30
```

### 3. Functions Stored in Dictionaries
Instead of long if/elif chains, store functions as dictionary values:

```python
# WITHOUT dictionary (tedious)
if operator == '+':
    result = add(n1, n2)
elif operator == '-':
    result = subtract(n1, n2)
elif operator == '*':
    result = multiply(n1, n2)
# ... grows with every operation

# WITH dictionary (elegant)
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# Access function by operator key
result = operations[operator](n1, n2)
# No if/elif needed! Calls the right function automatically
```

**Why it matters:** Functions are first-class objects (like integers, strings). You can store them, pass them around, and call them later.

### 4. Function Parameters vs Return Values
```python
def calculator_operation(n1, n2):
    """Parameters (inputs) vs Return (output)."""
    # n1, n2 are PARAMETERS (inputs)
    result = n1 + n2
    return result  # OUTPUT - handed back to caller

# Call it
answer = calculator_operation(5, 3)  # 5,3 are arguments (actual values)
#        argument               ^argument
#        passed to parameters   └──→ parameter n1 and n2
```

### 5. Nested Function Calls
One function can call another:
```python
def days_in_month(year, month):
    # CALL is_leap FROM WITHIN days_in_month
    if is_leap(year) and month == 2:
        return 29
    else:
        return 28

days = days_in_month(2024, 2)  # Calls is_leap internally
```

### 6. Docstrings (Documentation)
Functions can include a docstring describing purpose and usage:
```python
def add(n1, n2):
    """Add two numbers and return the sum."""
    return n1 + n2

# Accessing docstring
print(add.__doc__)  # "Add two numbers and return the sum."
help(add)  # Displays docstring in help system
```

### 7. Multiple Return Paths
A function can have multiple return statements:
```python
def is_leap(year):
    if year % 400 == 0:
        return True  # First exit
    if year % 100 == 0:
        return False  # Second exit
    if year % 4 == 0:
        return True  # Third exit
    return False  # Default exit
```

---

## Common Pitfalls

- **Forgetting the return statement:** Function computes correctly but returns `None` because no return statement
- **Printing instead of returning:** Function prints the answer but you can't use it in calculations
- **Not assigning the return value:** `add(5, 3)` runs but doesn't save result. Use `result = add(5, 3)`
- **Wrong parameter/argument count:** `add(5)` crashes (needs 2 arguments)
- **Complex nested calls hard to debug:** When functions call functions, errors are harder to trace
- **Type mismatches:** If function expects float but receives string, operations fail
- **Function references vs function calls:** `operations['+']` is the function; `operations['+']()` calls it

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 7** | Game loop with return values (instead of global state) |
| **Day 9** | Dictionaries to store data/operations |
| **Day 11** | Blackjack uses functions with return values heavily |
| **Day 15-16** | Coffee Machine uses function returns to update state |
| **Day 20+** | Methods in classes are functions with returns |

---

## Before You Move On
Make sure you can:
- [ ] Explain the difference between returning and printing
- [ ] Write a function that returns a value and use it in a calculation
- [ ] Trace through a function call with parameters and return values
- [ ] Store a function in a variable or dictionary
- [ ] Call a function stored in a dictionary
- [ ] Use nested function calls (one function calling another)
- [ ] Write a docstring for a function

---

## Practice Prompt
**Enhancement Challenge:**
1. Add more operations: power (`**`), modulo (`%`), floor division (`//`)
2. Create a function `validate_operator()` that checks if operator exists before calling
3. Add error handling: what if user divides by zero?
4. Create a `get_history()` function that returns all calculations done (store in list)
5. Implement `undo()` that removes the last calculation from history

**Advanced Challenge:**
```python
# Create a function that chains operations
def apply_operations(start_value, operations_list):
    """Apply a sequence of operations to a value."""
    # operations_list format: [('*', 2), ('+', 5), ('/', 3)]
    result = start_value
    for operator, operand in operations_list:
        result = operations[operator](result, operand)
    return result

# Usage:
final = apply_operations(10, [('*', 2), ('+', 5)])  # (10 * 2) + 5 = 25
```

**Bonus:** Implement the calculator with support for variables:
```python
variables = {}
# If user types: "x = 5 + 3", calculate and store x
# Then they can use x in future calculations
```
