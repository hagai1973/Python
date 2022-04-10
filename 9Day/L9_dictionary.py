programing_dictionary={
                       "Bug": "Indicate an error in software",
                       "Function":"code that do some task",
                       "Loop": "runing over and over until exit condtion"
                       }


# Gev value from dic.
print(programing_dictionary["Bug"])

programing_dictionary["Bug"] = "Indciate on errors in expected behaviour of the program"

print(programing_dictionary["Bug"])




for k in programing_dictionary:
    print(k + ": " + programing_dictionary[k])


#Wipe the dictionary
# programing_dictionary = {}