num_input = input("type two digit number (e.g 15):")
print("the type of your input is: " + str(type(num_input)))

str_number = str(num_input)
print("Typed number is: " + str_number)


n1 = int(str_number[0])
n2 = int(str_number[1])
Results = n1+n2
print("Result of combined your two numbers is: " + str(Results))