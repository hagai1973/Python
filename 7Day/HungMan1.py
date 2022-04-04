import random
from hungman_art import stages, logo
import word_list

# word_list = ["abruptly","luxury","numbskull","vixen","quiz","yoked","embezzle","peekaboo"]

word_selected = random.choice(word_list.word_list)
print(hungman_art.logo)
# word_selected = "numbskull"
word_length = len(word_selected)
limit = word_length +3
print(word_selected)

display = ""
for n in range(0,word_length):
    display+="_"
               
print (display)



# letterGuss = "l"
attempts = 0


while (("_" in display)and attempts<limit):
    
    letterGuss = input("Guess letter: \n").lower()
    
    while (letterGuss in display):
        letterGuss = input("Letter was already checked, guess new letter: \n").lower()
    
    attempts+=1
    counter = 0
    print("Checking: ")
    for element in range(0, word_length):
        # print(word_selected[element])
        found = False
        if letterGuss == word_selected[element]:
            display = display[:counter] + letterGuss + display[counter + 1:]
            found = True
        counter+=1
    if found:
            print(f"match: {display}")
            found = False
    else:
            print(f"No match: {display} the letter {letterGuss} is not in the word ")
    if "_" in display:
        print(f"you have {limit-attempts} more attmpts to guess the word missing {display.count('_')} chars")

if attempts<limit:
    print(f"You win: {display}")
else:
    print(f"You lost: {display} but it should be: {word_selected}")
