# Calculator
import art


# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide 
def divide(n1, n2):
    return n1 / n2

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              }


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    for k in operations:
        print(k)

    go_again = True

    while go_again:
        operator = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operator](num1, num2)~

        print(f"{num1} {operator} {num2} = {answer}")

        ask_to_go_again = input("Do you want to continue calculating? (Y/N): ").lower()
        if ask_to_go_again == 'y':
            num1 = answer
        else:
            go_again = False
            calculator()

calculator()