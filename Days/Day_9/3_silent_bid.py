from os import system

bidder_and_value = {}
cont = "y"

while cont == "y":
    print("Welcome to silent bid!")
    name = input("Enter your name: ")
    amount = int(input("Enter your bid: $"))
    bidder_and_value[name] = amount
    cont = input("press 'y' for more bidders ").lower()
    system("clear")

max = 0    
highest_bidder = ""
for key in bidder_and_value:
    if bidder_and_value[key] > max:
        max = bidder_and_value[key]
        highest_bidder = key
    
print(f"Highest bidder is {highest_bidder} for ${max}.")