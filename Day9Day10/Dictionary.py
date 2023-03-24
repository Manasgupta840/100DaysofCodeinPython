student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

print(student_scores["Harry"])
#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}
for scores in student_scores:
    if student_scores[scores]>90:
        student_grades[scores] = "Outstanding"
    elif student_scores[scores] > 80:
        student_grades[scores] = "Exceeds Expectations"
    elif student_scores[scores] > 70:
        student_grades[scores] = "Acceptable"
    else:
        student_grades[scores] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)