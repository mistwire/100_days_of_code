from pathlib import Path

# Path() creates a Path object -- it's a class (like Car from Day 1).
# read_text() is a method on that object, just like my_car.get_descriptive_name().
path = Path("pi_digits.txt")
contents = path.read_text()       # Returns the ENTIRE file as one big string
lines = contents.splitlines()     # Splits that string into a list, one element per line
print(lines)

# You can skip the temp variable and loop directly over splitlines().
# splitlines() returns a list, and you can iterate any list with `for`.
for line in contents.splitlines():
    print(line)

    