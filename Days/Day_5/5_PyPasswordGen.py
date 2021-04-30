import os
#Password Generator Project
from random import *
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("\n\nHi Sherin.\nWelcome to the Ashraf's Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# os.system('clear')

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pwd = ""

# for i in range (0, nr_letters):
#     x = randint(0, len(letters) - 1)
#     pwd += letters[x]
# for i in range (0, nr_symbols):
#     x = randint(0, len(symbols) - 1)
#     pwd += symbols[x]
# for i in range (0, nr_numbers):
#     x = randint(0, len(numbers) - 1)
#     pwd += numbers[x]
    
for i in range (0, nr_letters):
    pwd += choice(letters)
for i in range (0, nr_symbols):
    pwd += choice(symbols)
for i in range (0, nr_numbers):
    pwd += choice(numbers)
    
# print(pwd)   


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

l = list(pwd)
shuffle(l)
l = "".join(l)
print (f"This is a relly strong password {l}\n\n")