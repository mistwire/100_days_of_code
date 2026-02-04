from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

# Build one continuous string from all lines of the file.
# lstrip() removes leading whitespace from each line (the file has indented lines).
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()  # lstrip = "left strip" -- removes leading spaces/tabs

# Slice notation: pi_string[:52] gets the first 52 characters.
# This is the same indexing concept used for lists in Day 4.
print(f"{pi_string[:52]}...")
print(len(pi_string))

# The `in` operator checks if one string exists inside another.
# This works for any substring search -- very useful pattern.
birthday = input("Enter your birthday in the format mmddyy: ")
if birthday in pi_string:
    print("Your birthday is in the 1st million digits of pi!")
else:
    print("Your birthday is not in the 1st million digits of pi.")