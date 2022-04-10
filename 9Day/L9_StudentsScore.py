student_score = {"Harry": 81, 
                 "Ron": 100,
                 "Herminoe": 91,
                 "John": 71, 
                 "David": 70,
                 "Ben": 80,
                 }

student_grades = {}

for k in student_score:
    print(k + ": " + str(student_score[k]))
    if student_score[k] > 90:
        student_grades[k] = "Outstanding"
    elif student_score[k] > 80:
        student_grades[k] = "Exceedes Expectaions"
    elif student_score[k] > 70:
        student_grades[k] = "Acceptable"
    elif student_score[k] <= 70:
        student_grades[k] = "Fail"
    
    
for s in student_grades:
    print(s + ": " + str(student_grades[s]))
    
    