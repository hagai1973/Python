from random import randint, random
from random import seed

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_selection = int(input("Select 1=rock, 2=paper, 3=scissors: \n"))

print("Your selection")
if (your_selection)==1:
 print(rock)
elif (your_selection)==2:
 print(paper)
elif (your_selection)==3:
 print(scissors)
else:
 print("N/A selection")

print("Python selection")
python_selection = randint(1, 3)
if (python_selection)==1:
 print(rock)
elif (python_selection)==2:
 print(paper)
elif (python_selection)==3:
 print(scissors)
else:
 print("N/A selection")
 
if python_selection==your_selection:
 print("No winner...")
elif ((python_selection==1 and your_selection==3)or (python_selection==2 and your_selection==1) or (python_selection==3 and your_selection==2)):
 print("Computer win...")
else:
 print("You win...")