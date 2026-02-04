import art
import os

# KEY CONCEPT: Extended alphabet list to handle wraparound
# PATTERN: Letters A-Z are duplicated at the end for modular arithmetic wrapping
# When we shift Z by 1, alphabet.index('z') + 1 = 25 + 1 = 26, which accesses the second 'a'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  """Encode or decode text using the Caesar cipher algorithm."""
  end_text = ""
  # KEY CONCEPT: Reversibility - decoding means shifting backwards
  # This is why multiplying by -1 works: shift_amount becomes negative
  if cipher_direction == "decode":
    shift_amount *= -1

  # PATTERN: Check each character individually
  # Non-alphabetic characters pass through unchanged (spaces, punctuation, numbers)
  for char in start_text:
    if char in alphabet:
        # ALGORITHM: Find position -> Apply shift -> Get new letter
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]  # Extended alphabet handles wraparound
    else:
       # PRESERVATION: Keep non-letters as-is (spaces, digits, punctuation)
       end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

# Display the cipher logo at program start
print(art.logo)

# CONTROL FLOW: Loop allows user to run multiple encryptions without restarting
should_continue = True

while should_continue:
    os.system('clear')
    print(art.logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # MODULO OPERATOR: % normalizes shifts to 0-25 range
    # Why: Caesar cipher repeats every 26 letters. Shift of 45 = shift of 19 (45 % 26)
    # This prevents index errors and makes the cipher work with any shift value
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # REPLAYABILITY: Ask user if they want another round
    # Connection to Day 8 control flow: while loop pattern for continuous gameplay
    result = input("Do you want to go again? Type 'yes' or 'no'.\n")
    if result == 'no':
       should_continue = False
       print("Goodbye")