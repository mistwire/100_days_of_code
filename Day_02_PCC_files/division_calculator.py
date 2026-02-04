print("Give me 2 numbers & I'll devide them.")
print("Enter 'q' to quit")

# PATTERN: `while True` + `break` creates an infinite loop that only stops
# when a specific condition is met. You'll use this pattern a LOT in games
# (Days 7-12) and interactive programs.
while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break  # Exits the while loop entirely
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:
        # Two things could go wrong here:
        # 1. int() could fail if input isn't a number (ValueError)
        # 2. Division by zero (ZeroDivisionError)
        # Only ZeroDivisionError is caught -- a ValueError would still crash.
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't devide by 0!")
    else:
        print(answer)



