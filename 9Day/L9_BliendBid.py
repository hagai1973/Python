import os
import art
#clear
os.system('cls')
print(art.logo)

# Wipe the dictionary
auction_dictionary = {}
winner_bid = 0
winner_name = ""


def add_bid(bid_name, bid_amount):
    auction_dictionary[bid_name] = int(bid_amount)

def get_winner(dictionary):
    winner_bid = 0
    winner_name = ""
    for k in dictionary:
        # print(k + ": " + auction_dictionary[k])
        if int(dictionary[k]) > winner_bid:
            winner_bid = dictionary[k]
            winner_name = k                    
    return winner_name



print("Welcome to the secret auction program")
name = input("Type your name: \n")
bid = input("Type your bid: \n")

print(name, bid)
add_bid(name, bid)


more_bid = input("Do you want to add a bid ?  y/n \n")
while(more_bid=="y"):
    os.system('cls')
    name = input("Type your name: \n")
    bid = int(input("Type your bid: \n"))
    add_bid(name, bid)
    more_bid = input("Do you want to add a bid ?  y/n \n")


winner_name = get_winner(auction_dictionary)

print (auction_dictionary)
winner_bid = auction_dictionary[winner_name]
print (f"winner name: {winner_name}, winner_bid: {winner_bid} $")

