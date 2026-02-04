############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
import art

def deal_card():
    """Returns a random card from the deck."""
    # DECK SETUP: Four 10-value cards (J, Q, K count as 10) plus Ace as 11
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate total score, handling Ace logic and blackjack detection.
    Blackjack (21 with exactly 2 cards) returns 0 as a special code.
    """
    # BLACKJACK: Exactly 2 cards summing to 21 is special (return 0 to signal)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # ACE HANDLING: If Ace (11) causes bust (>21), convert to 1 instead
    # Key concept: Aces can be 1 OR 11 - player gets flexible choice
    # Strategy: Try 11 first, but if that busts, use 1 instead
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # Remove the Ace worth 11
        cards.append(1)   # Add Ace worth 1 instead

    return sum(cards)

def compare(user_score, computer_score):
    """Determine game outcome and return message."""
    # CHECK EACH WIN/LOSS CONDITION IN ORDER
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:  # Computer has blackjack
        return "Computer has blackjack, you lose!"
    elif user_score == 0:  # User has blackjack
        return "Player has blackjack, you win!"
    elif user_score > 21:  # User busted
        return "Player has busted, you lose!"
    elif computer_score > 21:  # Computer busted
        return "Computer has busted, you win!"
    elif user_score > computer_score:  # User closer to 21
        return f"Player got {user_score}, computer has {computer_score}: You win!"
    else:  # Computer closer to 21
        return f"Player got {user_score}, computer has {computer_score}: You lose!"

def play_game():
    """Main game loop: deal cards, let player hit/stand, dealer plays, determine winner."""
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # INITIAL DEAL: Each player gets 2 cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # PLAYER TURN: Let user decide to hit until they stand or bust
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # DISPLAY STATE: Show user's hand and dealer's first card (hide hole card)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        # END CONDITIONS FOR PLAYER TURN
        # Blackjack (score 0), computer blackjack, or player bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # PLAYER CHOICE: Hit (another card) or Stand (keep current hand)
            hit_again = input("Do you want to hit? (Y/N): ").lower()
            if hit_again == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # DEALER TURN: Computer automatically follows strict rules
    # KEY CONCEPT: Dealer must hit if score < 17 (standard Blackjack rule)
    # This creates dealer AI: predictable, non-strategic
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # SHOW RESULTS AND DETERMINE WINNER
    print(f"  Players final hand: {user_cards}, final score: {user_score}")
    print(f"  Computers final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# GAME LOOP: Ask if user wants another game
# Continues until user enters something other than 'y'
while input("Do you want to play a game of Blackjack? (Y/N): ").lower() == 'y':
    os.system('clear')
    play_game()

