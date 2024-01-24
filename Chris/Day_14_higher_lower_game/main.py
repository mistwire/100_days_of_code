from game_data import data
import art
import random 
import os

score = 0

def get_random_data():
    contestant = random.choice(data)
    return contestant

def compare():
    first_option = get_random_data()
    print(f"Compare A: {first_option['name']}, {first_option['description']}, from {first_option['country']}.")
    print(art.vs)
    second_option = get_random_data()
    print(f"Against B: {second_option['name']}, {second_option['description']}, from {second_option['country']}.")
    players_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if players_guess +


# TODO: print logo
os.system('clear') 
print(art.logo)



# TODO: compare number of followers to see who 'wins'



# TODO: increment the score or player loses and display final score

