import os
import art

# KEY CONCEPT: Dictionary stores key-value pairs (bidder_name: bid_amount)
# Unlike lists, dictionaries don't rely on index - we access by meaningful keys
bids = {}  # Empty dict to accumulate bids
go_again = True

# HELPER FUNCTION: Find the key (bidder name) given a value (bid amount)
# Problem: dict.values() gives us highest bid, but we need the NAME
# Solution: Iterate through items() to find matching value and return key
def get_key(val):
    for key, value in bids.items():
        if val == value:
            return key
    return "key doesn't exist"

print(art.logo)

# GAME LOOP: Collect multiple bids, storing each as it comes in
while go_again:
    bidder_name = input("What is your name?: ")
    bidder_price = float(input("What amount do you want to bid?: "))
    # KEY CONCEPT: Dictionary assignment - add new bid or update existing bidder
    bids[bidder_name] = bidder_price
    bid_again = input("Is there another bidder (Y/N)?: ")
    if bid_again == "Y":
        os.system('clear')
    else:
        go_again = False

# FINDING THE WINNER: Find the highest bid value, then look up who bid it
# ALGORITHM STEP 1: Get all bid amounts (ignore bidder names for now)
x = bids.values()
highest_bid = 0

# ALGORITHM STEP 2: Linear search to find maximum value
# Note: Could use built-in max(bids.values()) instead, but this shows the concept
for i in x:
    if i > highest_bid:
        highest_bid = i

# ALGORITHM STEP 3: Look up which bidder made the highest bid
print(f"Congrats! {get_key(highest_bid)} is the winner!")