print("Give me 2 numbers & I'll devide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / in(second_number)
    except ZeroDivisionError:
        print("You can't devide by 0!")
    else:
        print(answer)



