students_heights = [180, 124, 165, 173, 189, 169, 146]
n = len(students_heights)

for i in range(n-1):
 for j in range(0, n-i-1):
  if students_heights[j] > students_heights[j+1]:
   students_heights[j],students_heights[j+1] = students_heights[j+1],students_heights[j]
 
highest = students_heights[n-1]
print(f"the highest is {highest}")