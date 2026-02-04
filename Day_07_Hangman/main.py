#Step 5

import random
import hangman_art
import hangman_words
import os

# PATTERN: Importing custom modules (Day 7 key concept)
# These modules contain data (word_list, stages, logo) we'll use repeatedly
chosen_word = random.choice(hangman_words.word_list)  # RANDOM MODULE: select one word from our list
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Display the game logo at startup - ASCII art makes the game feel more polished
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Initialize display list with underscores - this is what the player sees
# KEY CONCEPT: Using a list to track revealed letters (list mutation in loop)
display = []
guessed_letters = []

for _ in range(word_length):
    display += "_"

# GAME LOOP: Core game mechanics - keep playing until win/loss condition
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    # LOGIC CHECK: Prevent penalty for re-guessing the same letter
    if guess in guessed_letters:
        print(f"You've already tried {guess}!")

    # PATTERN: Compare user's guess against each position in the word
    # This reveals all matching letters at once (like real Hangman)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  # Mutable list: update in place

    # KEY CONCEPT: Wrong guess handling - deduct lives and give feedback
    if guess not in chosen_word:
        print(f"{guess} is not in the secret word!")
        lives -= 1
        print(f"{lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    guessed_letters.append(guess)  # Track all guesses (including repeats) for logic check above

    # Display current state: join list elements with spaces for readability
    print(f"{' '.join(display)}")

    # WIN CONDITION: Check if all letters are revealed (no underscores left)
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Visual feedback: Show hangman ASCII art based on remaining lives
    # Index 0=6 lives (full man), Index 6=0 lives (dead)
    print(hangman_art.stages[lives])