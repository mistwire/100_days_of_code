from pathlib import Path

path = Path("pi_digits.txt")
# method chaining 
contents = path.read_text()
lines = contents.splitlines()
print(lines)

# you can remove the temp variable and loop directly over the splitlines() returned list:
for line in contents.splitlines():
    print(line)

    