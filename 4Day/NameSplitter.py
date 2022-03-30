from random import randint, random
from random import seed


# name_list = input("Type list of names seprated by comma: ")
name_list = "n1,n2,n3,n4"

list_name = name_list.split(",")

print (list_name)
print (len(list_name))
value = randint(0, len(list_name)-1)

print(value)
print(list_name[value])