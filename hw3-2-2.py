# Author: ATN 9/29/21

height = int(input("Please enter your current height in centimeters: "))
weight = int(input("Please enter your current weight in kilograms: "))
bmi = (weight / height / height) * 10000
if (bmi < 19):
    print("You are underweight. ")
elif (bmi < 25):
    print("You are healthy. ")
elif (bmi < 30):
    print("You are overweight. ")
elif (bmi < 40):
    print("You are obese. ")
elif (bmi > 40):
    print("You are extremely obese. ")
