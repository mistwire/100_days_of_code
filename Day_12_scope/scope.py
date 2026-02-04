################### Scope ####################

# GLOBAL SCOPE:
# Variables defined outside of any function or class have global scope.
# They can be accessed from any part of the code, both inside and outside functions.
# Global variables are typically declared at the top level of a script or module.
enemies = 1

def increase_enemies():
    # KEY CONCEPT: LOCAL SCOPE
    # Variables defined within a function have LOCAL scope.
    # They can only be accessed within the function where they are defined.
    # Local variables are created when the function is called and destroyed when the function exits.

    # SHADOWING: This creates a NEW local variable "enemies"
    # It doesn't modify the GLOBAL enemies variable above
    # Python searches: 1) Local scope first, 2) Global scope second
    enemies = 2
    print(f"enemies inside function: {enemies}")  # Prints 2 (local variable)

increase_enemies()
print(f"enemies outside function: {enemies}")  # Prints 1 (global variable unchanged)

# IMPORTANT: Python scope doesn't apply to for/while loops or if statements
# Those blocks DON'T create new scope! Variables leak out:
if True:
    x = 5
print(x)  # Works! Prints 5 (x is NOT limited to if block)

