from game_data import data
import art
import random 
import os

score = 0
game_continues = True

def get_random_data():
    contestant = random.choice(data)
    return contestant

first_option = get_random_data()

while game_continues:
    os.system('clear') 
    print(art.logo)
    print(f"Your current score is: {score}")
    print(f"Compare A: {first_option['name']}, {first_option['description']}, from {first_option['country']}.")
    print(f"cheat: {first_option['follower_count']}")
    print(art.vs)
    second_option = get_random_data()
    print(f"Against B: {second_option['name']}, {second_option['description']}, from {second_option['country']}.")
    print(f"cheat: {second_option['follower_count']}")
    players_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if first_option['follower_count'] > second_option['follower_count']:
        answer = 'a'
    else:
        answer = 'b'
    if players_guess == answer:
        score += 1
        first_option = second_option
    else:
        game_continues = False
        print(f"Game over, your final score is: {score}")

