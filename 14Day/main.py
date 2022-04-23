import random
import json
import sys
from game_data import data
import os
from art import logo
from art import vs


# clear screen and print begin game logo
os.system('cls')
print(logo)

# dumps the json object into an element
json_str = json.dumps(data)

# load the json to a string
resp = json.loads(json_str)

#Counting correct answers by the user
user_score = 0


# Get random item 
def get_random_number(up_to = 10):
    """get random number by range"""
    return random.randint(0, up_to)
 
def get_data_to_list(number = 0):
    details = []
    details.append(resp[number]['name'])
    details.append(resp[number]['follower_count'])
    details.append(resp[number]['description'])
    details.append(resp[number]['country'])
    return details


random_int_1 = get_random_number(len(resp)-1)
compare_A = get_data_to_list(random_int_1)

# print the first compare details
print("Compare A: " + compare_A[0] + ", "+ compare_A[2] + ", from " + compare_A[3] +".")

# Print vs graphic
print(vs)

# Get the second compare
random_int_2 = get_random_number(len(resp)-1)

# verify not same item to compare
while (random_int_2 == random_int_1):
    random_int_2 = get_random_number(len(resp)-1)
    
compare_B = get_data_to_list(random_int_2)
# print the second compare details
print("Compare B: " + compare_B[0] + ", "+ compare_B[2] + ", from " + compare_B[3] +".")


user_selection = input(f"Who has more followers? Type 'A' or 'B'").upper()





# print(f"random int: {random_int}")
# print the resp
# print (resp)
# print (resp[0]['name'])
# print (resp[0]['follower_count'])

# print (resp[49]['name'])
# print (resp[49]['follower_count'])
# print(len(resp))
