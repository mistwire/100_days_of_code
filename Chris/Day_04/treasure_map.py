line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Mark the grid map A1 -> C3:\n")  
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# My solution:
if position[0] == "A":
  if position[1] == "1":
    line1[0] = "X"
  elif position[1] == "2":
    line2[0] = "X"
  else:
    line3[0] = "X"
elif position[0] == "B":
  if position[1] == "1":
    line1[1] = "X"
  elif position[1] == "2":
    line2[1] = "X"
  else:
    line3[1] = "X"
elif position[0] == "C":
  if position[1] == "1":
    line1[2] = "X"
  elif position[1] == "2":
    line2[2] = "X"
  else:
    line3[2] = "X"

# Angela's solution:
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index] [letter_index] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")