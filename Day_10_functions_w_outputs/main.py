# Calculator
import art

# KEY CONCEPT: Functions with RETURN VALUES
# Each operation function takes two numbers and returns the result
# Return values allow functions to produce output without printing

def add(n1, n2):
    """Add two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divide two numbers."""
    return n1 / n2

# PATTERN: Store functions in a dictionary
# Operations dict maps operator symbols to function references
# This allows: operations['+'](5, 3) instead of if/elif chains
operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              }

def calculator():
    """Main calculator loop - get numbers and operators, compute results."""
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    # Display available operators
    for k in operations:
        print(k)

    go_again = True

    while go_again:
        operator = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))

        # KEY CONCEPT: Function reference lookup and calling
        # operations[operator] retrieves the function (not calling it yet)
        # (num1, num2) calls the function with arguments
        answer = operations[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        # CHAINING CALCULATIONS: Use result as first number for next operation
        ask_to_go_again = input("Do you want to continue calculating? (Y/N): ").lower()
        if ask_to_go_again == 'y':
            num1 = answer  # Carry forward result
        else:
            go_again = False
            calculator()  # Restart (allows new first number)

calculator()