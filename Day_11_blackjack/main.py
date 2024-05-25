############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
import art 

def deal_card ():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """Takes a list of cards as input and calculates the total score. If the total score is 21, it returns 0.
    Otherwise, it returns the total score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has blackjack, you lose!"
    elif user_score == 0:
        return "Player has blackjack, you win!"
    elif user_score > 21:
        return "Player has busted, you lose!"
    elif computer_score > 21:
        return "Computer has busted, you win!"
    elif user_score > computer_score:
        return f"Player got {user_score}, computer has {computer_score}: You win!"
    else:
        return f"Player got {user_score}, computer has {computer_score}: You lose!"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_again = input("Do you want to hit? (Y/N): ").lower()
            if hit_again == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) 

    print(f"  Players final hand: {user_cards}, final score: {user_score}")
    print(f"  Computers final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? (Y/N): ").lower() == 'y':
    os.system('clear')
    play_game()

