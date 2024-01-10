################### Scope ####################

# Global Scope:
# Variables defined outside of any function or class have a global scope.
# They can be accessed from any part of the code, both inside and outside functions.
# Global variables are typically declared at the top level of a script or module.
enemies = 1

def increase_enemies():
  # Local scope:
  # Variables defined within a function or a block of code have a local scope.
  # They can only be accessed within the function or block where they are defined.
  # Local variables are created when the function is called and destroyed when the function exits.
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# This only applies to functions and classes, not for/while loops, or if statements (Python doesn't have Block Scope)

