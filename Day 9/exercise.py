student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for students, score in student_scores.items():
    if score >= 91 and score <= 100:
        grade = "Outstanding" 
    elif score >= 81 and score <= 90:
        grade = "Exceeds Expectations" 
    elif score >= 71 and score <= 80:
        grade = "Acceptable" 
    elif score <= 70:
        grade = "Fail" 
    
    student_grades[students] = grade

print(student_grades)
