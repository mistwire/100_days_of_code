from pathlib import Path

path = Path("pi_digits.txt")
# method chaining 
contents = path.read_text()
lines = contents.splitlines()
print(lines)
for line in lines:
    print(line)

    