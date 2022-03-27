print("Welcome to the roolecoster!")

height = int(input("What is your height in cm ? ") )

if height >= 120:
 print("You can ride the attraction")
 age = int(input("What is your age ? ") )
 if age > 18:
  print("You should pay: $12")
 elif age >= 12 and age <= 19:
   print("You should pay: $7")
 else:
  print("You should pay: $5")
 
 
else:
 print("You can not get in to the attraction")
