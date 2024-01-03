print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_amount = 0
if size == 'S':
  total_amount += 15
elif size == "M":
  total_amount += 20
elif size == "L":
  total_amount += 25
if add_pepperoni == 'Y' and size == "S":
  total_amount += 2
if add_pepperoni == "Y" and size == "M":
  total_amount += 3
if add_pepperoni == "Y" and size == "L":
  total_amount += 3
if extra_cheese == "Y":
  total_amount += 1

print(f"Your final bill is: ${total_amount}.")