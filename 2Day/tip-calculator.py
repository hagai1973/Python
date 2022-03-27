print("Welcome to the tip calculator !!!")
total_bill = float(input("What was the total bill: $ "))

print(f"Total bill is: $ {total_bill} ")

precentag_tip = int(input("How much tip you want to give (10%,12%,15%)  "))

print(f"% tip is: {precentag_tip} %")

numbers_pays = int(input("How many are paying: "))

print(f"Number of payers: {numbers_pays} ")

total_include_tip = total_bill + (total_bill*(precentag_tip/100))
print(f"Total cost with tip is: {total_include_tip} ")

each_need_to_pay = "{:.2f}".format(round(total_include_tip/numbers_pays,2))
print(f"Each one need to pay: $ {each_need_to_pay} ")