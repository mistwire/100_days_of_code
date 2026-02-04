import os
import art
import random

def game():
    """Main game loop for the Higher/Lower guessing game."""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # SCOPE: These variables are LOCAL to the game() function
    # They only exist while game() is running
    # Each time game() is called, new local vars are created
    if difficulty == 'easy':
        guesses = 10
    else:
        guesses = 5

    number = random.randint(1, 100)
    print(f"the secret number is {number}")

    # GAME LOOP: Keep asking for guesses while attempts remain
    while guesses > 0:
        guess = int(input(f"You have {guesses} attempts remaining to guess the number.\nMake a guess:  "))

        if guess == number:
            print(f"You got it! The answer was {number}")
            break  # Exit loop early on success
        elif guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")

        # DECREMENT: Reduce attempts after wrong guess
        guesses -= 1
        if guesses == 0:
            print("You've run out of guesses! You lose.")

game() 