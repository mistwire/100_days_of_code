#Password Generator Project
import random

# CHARACTER POOLS: Three separate lists to pick from.
# Each pool ensures the password has a mix of character types.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# randint(a, b) returns a random integer where a <= result <= b (both inclusive).
# This means password length varies between 12-18 characters total.
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# STEP 1: COLLECT -- Pick random characters from each pool
password_list = []

for char in range(nr_letters):
  # .append() adds one item to the list. Clearest way to add a single element.
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  # += on a list with a single-char string works here, but .append() is safer.
  # With multi-char strings, += would add each character separately.
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

# STEP 2: SHUFFLE -- Randomize order so character types are mixed.
# Without this, the password would always be: letters...symbols...numbers
# shuffle() modifies the list IN PLACE and returns None.
random.shuffle(password_list)

# STEP 3: JOIN -- Convert list of characters into a single string.
# Pythonic alternative: password = "".join(password_list)
password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")