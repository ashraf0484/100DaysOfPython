height  = (float(input("Enter your height in cm : ")))/100
weight = float(input("Enter your weight in cm : "))

bmi = round (weight / height ** 2, 2)
# rounded_bmi = round(bmi)

if bmi <= 18.5 :
    print(f"Your BMI is {bmi} and you are underweight ")
elif bmi <= 25:
    print(f"Your BMI is {bmi} and you have normal weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi} and you are overweight ")
elif bmi <= 35:
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are clinically obese")