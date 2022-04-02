students_heights = [180, 124, 165, 173, 189, 169, 146]

# print (len(students_heights))
total_hights = 0
counter = 0

for student in students_heights:
 total_hights += student
 counter +=  1
 
 # print(total_hights)
 
# average_heights = round(total_hights/len(students_heights),0)
average_heights = round(total_hights/counter)
print (f"the average height of the class is: {average_heights}")