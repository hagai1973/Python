import os
import art
import random

os.system('cls')
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def guess_number(game_level = 'e'):
    counter = 0
    do_found = False
    if game_level == "h":
        number_of_attempts = 5
    else:
        number_of_attempts = 10
    # print (random_number)
    # print (number_of_attempts)
    
    while ( (not do_found) and (number_of_attempts > 0)):
        counter += 1 
        user_guess = int (input (f"Guess number between 1-100, you have {number_of_attempts} more attmpts: \n "))
        
        if (user_guess > random_number):
            number_of_attempts -= 1
            print(f"Your guess is too high, try smaller number...you have only {number_of_attempts} more attempts")
            
            
        elif (user_guess < random_number):
            number_of_attempts -= 1
            print(f"Your guess is too small, try higher number...you have only {number_of_attempts} more attempts")
                
        else:
            print(f"******  Your guess is exact as the random number: {random_number}...you did it in {counter}  attempts")
            do_found = True
         
         
    if not do_found:
            print("You lost...sorry....")   
            
def get_random_number():
    return random.randint(1, 101)

def get_game_level():
    level = input("Choose a difficulty: Hard / Easy (H/E) \n").lower()
    if not level =="h" and not level =="e":
        level ="e"
    return level


# random_number = 6
# print(f"random number: {random_number}" )

continue_pleay = "y"
while continue_pleay == "y":
    game_level = get_game_level()
    random_number = get_random_number()
    guess_number(game_level)
    continue_pleay = input (f"Do you want to play again ? (y/n) \n ")
    

print("Thank you and see you soon...")

# while (number_of_attempts > 0 and not do_found):
#     print(f"number_of_attempts: {number_of_attempts}" )
    
