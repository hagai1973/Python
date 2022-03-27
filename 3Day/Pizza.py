print("Welcome to pizza machine")
size = input("Select pizza size: s/m/l: ")
add_pepperoni = input("Do you want pepperoni? (y/n): ")
extra_cheese = input("Do you want extra cheese? (y/n): ")
price = 0

if size.lower()=='s':
 price=15
 if add_pepperoni=='y':
  price+=2
elif size.lower()=='m':
 price=20
 if add_pepperoni=='y':
  price+=3
elif size.lower()=='l':
 price=25
 if add_pepperoni=='y':
  price+=3
else:
 print("Could not recongized your selection, small size was selected")
 price=15

if extra_cheese=='y':
  price+=1

print(f"your final bill is: {price}")