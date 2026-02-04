# 2D LIST (list of lists): Each line is a row, `map` holds all rows.
# Access any cell with map[row][col] -- e.g., map[0][2] = line1's 3rd element.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Mark the grid map A1 -> C3:\n")  
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# MY SOLUTION (verbose approach):
# Handles each of the 9 grid positions with explicit nested if/elif.
# Works correctly but repetitive -- with a larger grid this wouldn't scale.
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

# CONCISE SOLUTION (computed indexing):
# Instead of checking every case, CONVERT the input into list indices.
# This handles all 9 positions in 4 lines. Would work for any grid size.
letter = position[0].lower()           # Normalize to lowercase for safety
abc = ["a", "b", "c"]
letter_index = abc.index(letter)        # .index() returns position: "a"->0, "b"->1, "c"->2
number_index = int(position[1]) - 1     # int() converts string to number, -1 for zero-based indexing
map[number_index] [letter_index] = "X"  # One line replaces all 9 branches above


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")