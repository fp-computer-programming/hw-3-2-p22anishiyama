# Author: ATN 9/29/21

student_grade = float(input("What is your average for this quarter? "))

if (student_grade < 60):
    print("Your grade is an 'F'")
elif(student_grade <= 64.999):
    print("Your grade is a 'D'")
elif(student_grade <= 69.999):
    print("Your grade is a 'D+'")
elif(student_grade <= 72.999):
    print("Your grade is a 'C-'")
elif(student_grade <= 76.999):
    print("Your grade is a 'C'")
elif(student_grade <= 79.999):
    print("Your grade is a 'C+'")
elif(student_grade <= 82.999):
    print("Your grade is a 'B-'")
elif(student_grade <= 86.999):
    print("Your grade is a 'B'")
elif(student_grade <= 89.999):
    print("Your grade is a 'B+'")
elif(student_grade <= 92.999):
    print("Your grade is an 'A-'")
elif(student_grade <= 96.999):
    print("Your grade is an 'A'")
elif(student_grade <= 100):
    print("Your grade is an 'A'")
