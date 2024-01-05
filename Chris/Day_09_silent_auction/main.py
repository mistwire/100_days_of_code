import os
import art

bids = {}
go_again = True 
def get_key(val):
    for key, value in bids.items():
        if val == value:
            return key
    return "key doesn't exist"

print(art.logo)

while go_again:
    bidder_name = input("What is your name?: ")
    bidder_price = float(input("What amount do you want to bid?: "))
    bids[bidder_name] = bidder_price
    bid_again = input("Is there another bidder (Y/N)?: ")
    if bid_again == "Y":
        os.system('clear')
    else:
        go_again = False

x = bids.values()
highest_bid = 0
for i in x:
    if i > highest_bid:
        highest_bid = i

print(f"Congrats! {get_key(highest_bid)} is the winner!")