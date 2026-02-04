# How to modify a global variable inside a function:

# APPROACH 1: Using 'global' keyword (NOT RECOMMENDED)
enemies = 1

def increase_enemies():
    # WARNING: The 'global' keyword tells Python to modify the global variable
    # This breaks encapsulation and makes code hard to reason about
    # Avoid using 'global' except in rare cases
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# Output: inside=3, outside=3 (global was actually modified)

print("\n" + "="*50 + "\n")

# APPROACH 2: Using return values (RECOMMENDED)
# This is cleaner and more predictable
enemies = 1

def increase_enemies():
    # KEY CONCEPT: Don't modify globals, just compute new value
    # Let the CALLER decide whether to update their variable
    print(f"enemies inside function: {enemies}")  # Can still READ global
    return enemies + 1

# CALLER controls what to do with the returned value
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
# Output: inside=1, outside=2 (caller chose to update)

# WHY Approach 2 is better:
# 1. Function is predictable - doesn't have hidden side effects
# 2. Function can be tested independently
# 3. Caller explicitly chooses to update (clear intent)
# 4. Function can be reused in different contexts

