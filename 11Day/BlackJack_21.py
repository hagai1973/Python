import random
import os

os.system('cls')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_1 = []
the_house = []

def select_random_from_array(arr = cards):
    item = random.randint(0, len(arr) - 1)
    return arr[item]

def get_card(arr = player_1):
    return arr.append(select_random_from_array(cards))

def sum_list_cards(arr=player_1):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum

get_card(player_1)
print (f"player 1 card is:  {player_1[0]}")
get_card(the_house)
print (f"player 2 card is:  {the_house[0]}")
get_card(player_1)
cards_sum_player1 = sum_list_cards(player_1)
print (f"your cards are:  {player_1}, the sum of the cards is: {cards_sum_player1}")
to_contiue = input("Do you want to take another card: y/n \n ")

if (to_contiue=="y"):
    get_card(player_1)
    cards_sum_player1 = sum_list_cards(player_1)
    print (f"your cards are:  {player_1}, the sum of the cards is: {cards_sum_player1}")


