print("\n\nWelcome to tip calculator cum bill splitter")
bill = float(input("Enter the total bill : "))
tipPercent = int(input("What percent do you wanna tip? : "))
noOfPeople = int(input("No. of people to split the bill with : "))

perPerson = (bill * (tipPercent / 100) + bill) / noOfPeople

#roundPerPerson = round(perPerson, 2)
roundPerPerson = "{:.2f}".format(perPerson)

print(f"Each person has to pay {(roundPerPerson)} Dhs ")
