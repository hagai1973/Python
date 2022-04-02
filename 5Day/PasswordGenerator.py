import random

how_long = 20
number_amount = 6
symbol_amount = 6

new_password = ""
new_password_numbers = ""
new_password_symbol = ""


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','?']

letters_len = len(letters)
number_len = len(numbers)
symbols_len = len(symbols)

number_counter = 0
symbol_counter = 0


for n in range(0, number_amount):
 rand_num = random.randint(0,number_len-1)
 new_password_numbers = new_password_numbers + numbers[rand_num]

for s in range(0, symbol_amount):
 rand_num = random.randint(0,symbols_len-1)
 new_password_symbol = new_password_symbol + symbols[rand_num]


for n in range(0, how_long):
 rand_num = random.randint(0,letters_len-1)
 new_password = new_password  + letters[rand_num]
 
flag = True
counter = 0
while(flag):
  rand_num = random.randint(0,how_long-1)
  if new_password[rand_num] in letters:
   letter_to_replace  = new_password[rand_num]
   number_to_replace = new_password_numbers[counter]
   new_password = new_password.replace(letter_to_replace,number_to_replace,1)
   counter+=1
   if counter==number_amount:
    flag = False
   
flag = True
counter = 0
while(flag):
  rand_num = random.randint(0,how_long-1)
  myLetter = new_password[rand_num]
  if new_password[rand_num] in letters:
   new_password = new_password.replace(new_password[rand_num],new_password_symbol[counter],1)
   counter+=1
   if counter==symbol_amount:
    flag = False

print(f"the password is: {new_password}")