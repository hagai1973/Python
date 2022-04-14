import random
import art
import os



def play_game():
    os.system('cls')
    print(art.logo)
    keep_check = True

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_1 = []
    dealer = []

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

    def replace_ace(arr = player_1):
        sum_of_arr = 0
        for i in range (len(arr) - 1):
            sum_of_arr = sum_list_cards(arr)
            if arr[i] == 11 and sum_of_arr > 21:
                arr[i] = 1
        return arr


    cards_sum_dealer = 0
    cards_sum_player1 = 0

    #first card for you
    get_card(player_1)
    print (f"player 1 card is:  {player_1[0]}")

    #first card for dealer
    get_card(dealer)
    print (f"dealer card is:  {dealer[0]}")

    #second card for you
    get_card(player_1)
    cards_sum_player1 = sum_list_cards(player_1)


    if 11 in player_1:
            player_1 = replace_ace(player_1)
            cards_sum_player1 = sum_list_cards(player_1)

    print (f"player 1 second card is:  {player_1[-1]}, sum of the cards is: {cards_sum_player1}")


    to_contiue="y"

    if cards_sum_player1 == 21:
        to_contiue = "n"
        print (f"your cards are:  {player_1}, the final sum of yours cards is: {cards_sum_player1}, Lets see what the dealer do...")

    if to_contiue == "y":
        to_contiue = input("Do you want to take another card: y/n \n ").lower()

    #loop of cards until stopping or exeeding 21
    while (to_contiue=="y") and (cards_sum_player1 < 21):
        get_card(player_1)
        cards_sum_player1 = sum_list_cards(player_1)
        # print (f"your cards are:  {player_1}, the sum of yours cards is: {cards_sum_player1}")
        if cards_sum_player1 == 21:
            to_contiue = "n"
            # print (f"your cards are:  {player_1}, the final sum of yours cards is: {cards_sum_player1}, Lets see what the dealer do...")
            break
        if int(cards_sum_player1) < 21:
            print (f"1. your cards are:  {player_1}, the sum of yours cards is: {cards_sum_player1}")
            # to_contiue = input("Do you want to take another card: y/n \n ").lower()
        else:
            if 11 in player_1:
                player_1 = replace_ace(player_1)
            else:
                to_contiue = "n"
        cards_sum_player1 = sum_list_cards(player_1)
        if cards_sum_player1 > 21:
            break
        else:
            # print (f"your cards are 2:  {player_1}, the sum of yours cards is: {cards_sum_player1}")
            to_contiue = input("Do you want to take another card: y/n \n ").lower()
                
    if int(cards_sum_player1) > 21:
        print (f"The final sum of yours cards is: {cards_sum_player1}, your cards {player_1},  You Lost !!!")
        keep_check = False
    else:
        print (f"your cards are:  {player_1}, the final sum of yours cards is: {cards_sum_player1}, Lets see what the dealer do...")
        get_card(dealer)
        print (f"dealer next card is:  {dealer[-1]}")
        if 11 in dealer:
                dealer = replace_ace(dealer)
        cards_sum_dealer = sum_list_cards(dealer)
        print (f"Dealer cards are:  {dealer}, the sum of dealer cards is: {cards_sum_dealer}")
 
    while (cards_sum_dealer < 17 or cards_sum_dealer < cards_sum_player1) and (keep_check == True):
        get_card(dealer)
        cards_sum_dealer = sum_list_cards(dealer)
        print (f"dealer next card is:  {dealer[-1]}, sum of dealers card is: {cards_sum_dealer}")
        cards_sum_dealer = sum_list_cards(dealer)
        if cards_sum_dealer > 21:
            if 11 in dealer:
                dealer = replace_ace(dealer)
                cards_sum_dealer = sum_list_cards(dealer)
            else:
                print (f"Dealer cards are:  {dealer}, the sum of dealer cards is: {cards_sum_dealer}")
        elif cards_sum_dealer < cards_sum_player1:
            while (cards_sum_dealer < cards_sum_player1) and (cards_sum_dealer < 22):
                get_card(dealer)
                print (f"dealer next card is:  {dealer[-1]}")
                cards_sum_dealer = sum_list_cards(dealer)
                if cards_sum_dealer > 21:
                        if 11 in dealer:
                            dealer = replace_ace(dealer)
                            cards_sum_dealer = sum_list_cards(dealer)
                print (f"Dealer cards are:  {dealer}, the sum of dealer cards is: {cards_sum_dealer}")
    
    if (cards_sum_dealer > cards_sum_player1) and (cards_sum_dealer < 22) and keep_check == True:
        print (f"The final sum of yours cards is: {cards_sum_player1}, the final cards sum of the dealer is {cards_sum_dealer}, You Lost !!!")
        keep_check = False
    elif cards_sum_dealer == cards_sum_player1 and  keep_check == True:
        print (f"The final sum of yours cards is: {cards_sum_player1}, the final cards sum of the dealer is {cards_sum_dealer}, Draw !!!")
        keep_check = False
    elif keep_check == True:
        print (f"The final sum of yours cards is: {cards_sum_player1}, the final cards sum of the dealer is {cards_sum_dealer}, delar card are: {dealer} , You Win !!!")



play_game()
another_game = input("Do you want to play game ? y/n \n")
while (another_game == "y"):
    play_game()
    another_game = input("Do you want to play game ? y/n \n")
