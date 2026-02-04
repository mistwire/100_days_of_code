import art
import os

print(art.logo)

# KEY CONCEPT: Dictionary for storing data with meaningful keys
# Structure: {name: bid_amount, name: bid_amount, ...}
bids = {}
bidding_finished = False

# FUNCTION PATTERN: Encapsulates the winner-finding logic
# Takes bidding_record (dict) as parameter - generic and reusable
# This is cleaner than doing it inline (separation of concerns)
def find_highest_bidder(bidding_record):
    """Find and announce the highest bidder."""
    highest_bid = 0
    winner = ""
    # ITERATION: Loop through dictionary keys (bidder names)
    # Access values using key-based lookup: bidding_record[bidder]
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        # Track both the maximum BID and WHO made it
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

# GAME LOOP: Collect bids until done
while not bidding_finished:
    name = input("What is your name? :")
    price = int(input("What is your bid? $"))
    # DICTIONARY UPDATE: Add or overwrite entry for this bidder
    bids[name] = price
    should_continue = input("Are there any other bids? (Y/N): ")
    if should_continue == 'N':
        bidding_finished = True
        find_highest_bidder(bids)  # Pass entire dict to function
    elif should_continue == 'Y':
        os.system('clear')
    

