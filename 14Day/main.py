import random
import json
import sys
from game_data import data
import os
from art import logo, vs


# dumps the json object into an element
json_str = json.dumps(data)

# load the json to a string
resp = json.loads(json_str)

# Get random item 
def get_random_number(up_to = 10):
    """get random number by range"""
    return random.randint(0, up_to)
 
def get_data_to_dic(number = 0):
    """transfer json item to dictinary"""
    selection = {
    "name": resp[number]['name'],
    "count": resp[number]['follower_count'],
    "description": resp[number]['description'],
    "country": resp[number]['country'],
    }
    
    return selection

def print_compare(title = "A", dic={}):
    """print the dictionary data without count of followers"""
    print(f"Compare {title}: " + dic.get("name") + ", "+ dic.get("description") + ", from " + dic.get("country") +".")

def verify_user_answer(user_selection = 'A', dic_a={} ,dic_b={}):
    """Check if guess is correct or not"""
    if (dic_a.get("count") > dic_b.get("count")) and user_selection == "A" :
        return True
    elif (dic_a.get("count") < dic_b.get("count")) and user_selection == "B" :
        return True
    else:
        return False

want_new_game = True

while (want_new_game):
    # clear screen and print begin game logo
    os.system('cls')
    print(logo)
    #Counting correct answers by the user
    user_score = 0
    reset_game = False
    first_raound = True

    while (not reset_game):
        
        if (first_raound):       
            #Get random number    
            random_int_1 = get_random_number(len(resp)-1)
        else:
            random_int_1 = random_int_2
        
        #Get data from json by the random item number 
        compare_A = get_data_to_dic(random_int_1)

        # print the first compare details
        print_compare("A", compare_A)

        # Print vs graphic
        print(vs)


        # Get the second compare
        random_int_2 = get_random_number(len(resp)-1)

        # verify not same item to compare
        while (random_int_2 == random_int_1):
            random_int_2 = get_random_number(len(resp)-1)

        #Get data from json by the random item number 
        compare_B = get_data_to_dic(random_int_2)

        # print the second compare details
        print_compare("B", compare_B)

        #Get the user guess
        user_selection = input(f"Who has more followers? Type 'A' or 'B' \n").upper()
        
        if (verify_user_answer(user_selection, compare_A,compare_B)):
            os.system('cls')
            print(logo)
            user_score += 1
            print(f"You are right! current score: {user_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            reset_game = True
        
            #Not first guess: need to keep second guess as first
        first_raound = False
    
    # Check if user want new game
    answer = input("Do you want to play again ?  Y/N  \n").upper()
    if answer == "Y":
        want_new_game = True
    else: 
        want_new_game = False
    
    
    
    
    
    
# print(f"random int: {random_int}")
# print the resp
# print (resp)
# print (resp[0]['name'])
# print (resp[0]['follower_count'])

# print (resp[49]['name'])
# print (resp[49]['follower_count'])
# print(len(resp))
