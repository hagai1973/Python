import pyfiglet
import art
import os


# print(art.logo)

#Add
def add(n1=2, n2=2):
    """add numbers"""
    return n1 + n2
#multi
def multiply(n1=2, n2=2):
    """multiply numbers"""
    return n1 * n2
#Subtract
"""Minus numbers"""
def subtract(n1=2, n2=2):
    return n1 - n2
#divide
"""divide numbers"""
def divide(n1=2, n2=2):
    return n1 / n2

operation_dictionary = {"+": add,
                        "*": multiply,
                        "-": subtract,
                        "/": divide
                        }

def claculater():
    os.system('cls')
    result = pyfiglet.figlet_format("Calc", font = "doh")
    print(result)
    counter = 0 
    to_stop = False

    while not (to_stop):
        if counter == 0: 
            num1 = float (input("type first number: \n"))
            counter += 1
        
        print ("\n")
        for o in operation_dictionary:
            print (o + "\n")
        print ("\n")
        
        operation = input("type operation from above: (+,-,/,*)\n")
        num2 = float (input("type second number: \n"))
        result_calc = float (round(operation_dictionary[operation](num1,num2)))
        print (f"Calc result: {num1} {operation} {num2} = {result_calc}")
        answer = input("Do you want to continue calculate with results ? type: y/n or q to quite \n")
        if  answer == "n":
            claculater()
        elif answer == "q": 
            to_stop = True
        else:
            num1 = float(result_calc)

claculater()