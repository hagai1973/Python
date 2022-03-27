import random

for x in range(4):
 # Get random number between 1 to 2 (1=head, 2=tail)
 random_number = random.randint(1, 2)
 # Get number between 1 to 2 from user (1=head, 2=tail)
 your_bet = int(input("Select 1 for heads or 2 for tails: "))

 if (your_bet== random_number):
  print(f"You were right! ({your_bet} vs. {random_number} )")
 else:
  print(f"You were failed ({your_bet} vs. {random_number} )")
