from random import randint
from art import logo

# GLOBAL SCOPE: CONSTANTS
# These are defined at module level (outside functions)
# CONVENTION: All-caps names signal "this value shouldn't change"
# ACCESSIBILITY: Readable by all functions without modification
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Check user's guess and return remaining turns.
    KEY CONCEPT: Return values modify state without using 'global' keyword.
    This is better than modifying global variables.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1  # Return new value
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns  # Return unchanged (though game will exit)

def set_difficulty():
    """Get difficulty and return appropriate number of turns."""
    # SCOPE: Uses module-level constants (EASY_LEVEL_TURNS, HARD_LEVEL_TURNS)
    # These are GLOBAL but we're not modifying them - just reading
    # This is SAFE and CLEAN
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS  # Access global constant
    else:
        return HARD_LEVEL_TURNS  # Access global constant

def game():
    """Main game loop."""
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    # SCOPE: 'turns' is LOCAL to game()
    # Each call to game() gets fresh local variables
    turns = set_difficulty()  # Returns either 10 or 5

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # PATTERN: Update local variable from function return
        # Instead of: global turns; turns -= 1
        # Better: turns = check_answer(guess, answer, turns)
        turns = check_answer(guess, answer, turns)

        # Check if out of guesses
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return  # Exit game
        elif guess != answer:
            print("Guess again.")
