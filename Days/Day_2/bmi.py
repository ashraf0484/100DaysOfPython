print("\n\nWelcome to BMI calculator")

h = float(input("Enter your height(CM): "))
h = h / 100
w = int(input("Enter your weight(KG): "))

bmi = w / h ** 2

print(f"Your BMI is {int(bmi)}")
