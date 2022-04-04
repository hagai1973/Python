import random
from turtle import clear
import hungman_art
import word_list
import os
from hungman_art import stages



# word_list = ["abruptly","luxury","numbskull","vixen","quiz","yoked","embezzle","peekaboo"]

#Print game logo from art file
print(hungman_art.logo)
# Set test_mode True/False
test_mode = True

# Get random word from word list
word_selected = random.choice(word_list.word_list)


#Print the selected word - in test mode
if test_mode:
    print(word_selected)

#Get the selected word lenght
word_length = len(word_selected)

# Set the limit of tring possible: number of words + 3 false attempts
limit = 6


# Set the display string which show user guessing progress, initilize string with _
display = ""
for n in range(0,word_length):
    display+="_"
               
print (display)



# Set number of used attempts by user
attempts = 0

#Create new string which will include all the letters user will guess
total_letters_guessed = ""

# Loop until user guess the word or run out of guessing
while (("_" in display)and attempts < limit):
    
    #Get the guess letter
    letterGuss = input("Guess letter: \n").lower()
    os.system('cls')
  
    #If user already guess the letter so no progress
    while (letterGuss in total_letters_guessed):
        letterGuss = input("Letter was already checked, guess new letter: \n").lower()
    
    total_letters_guessed += letterGuss 

    found = False
    lettersFound = 0
    counter = 0
    print("Checking: ")
    for element in range(0, word_length):
        # print(word_selected[element])
        if letterGuss == word_selected[element]:
            display = display[:counter] + letterGuss + display[counter + 1:]
            found = True
            lettersFound+=1
        counter+=1
        
    if found:
            print(f"{lettersFound} bingo : {display}")
            found = False
    else:
            print(f"No match: {display} the letter {letterGuss} is not in the word ")
            limit-=1

            # Get the number of limit and attemtps for printing stage
            
            print(stages[limit])

    if "_" in display:
        print(f"you have {limit-attempts} more attmpts to guess the word missing {display.count('_')} chars")

# if guess all word and limit is greater then the attemtps
if attempts<limit:
    print(f"You win: {display}")
else:
    print(f"You lost: {display} but it should be: {word_selected}")
