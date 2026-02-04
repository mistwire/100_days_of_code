# PATTERN: Module separation -- data, art, and logic each live in their own file.
# This is the same principle used in Day 15 (coffee machine) and refined in Day 16 (OOP).
from game_data import data
import art
import random
import os

score = 0
game_continues = True

def get_random_data():
    # KEY CONCEPT: random.choice() works on any sequence -- here it picks a full dictionary
    # from a list of dictionaries. Same function as Day 5 (password chars) and Day 11 (cards).
    contestant = random.choice(data)
    return contestant

# Pick the first option outside the loop so we have something to start with.
# After each correct guess, the winner "carries forward" (see below).
first_option = get_random_data()

while game_continues:
    os.system('clear')
    print(art.logo)
    print(f"Your current score is: {score}")
    # PATTERN: Accessing dictionary values with bracket notation -- same as Day 9 (silent auction).
    # Each entry in `data` has the same keys, so it behaves like a database row.
    print(f"Compare A: {first_option['name']}, {first_option['description']}, from {first_option['country']}.")
    print(f"cheat: {first_option['follower_count']}")
    print(art.vs)
    second_option = get_random_data()
    print(f"Against B: {second_option['name']}, {second_option['description']}, from {second_option['country']}.")
    print(f"cheat: {second_option['follower_count']}")
    players_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # KEY CONCEPT: Separate "compute the answer" from "check the guess" --
    # this makes the logic easier to read and debug.
    if first_option['follower_count'] > second_option['follower_count']:
        answer = 'a'
    else:
        answer = 'b'
    if players_guess == answer:
        score += 1
        # PATTERN: "Carry forward" -- the winning option becomes next round's option A.
        # This creates continuity between rounds instead of two fresh random picks each time.
        first_option = second_option
    else:
        game_continues = False
        print(f"Game over, your final score is: {score}")

