# Calculator

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

num1 = int(input("What's the first number?: "))

for k in operations:
    print(k)

operator = input("Pick an operator from the lines above: ")

num2 = int(input("What's the second number?: "))

answer = operations[operator](num1, num2)

print(f"{num1} {operator} {num2} = {answer}")
