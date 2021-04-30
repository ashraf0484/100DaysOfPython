#Name of your colleagues or friends
names_string = input("Give me everybody's names, separated by a comma. ")

#Splits the string to a list
names = names_string.split(", ")

import random

no_of_names = len(names)
random_payer = random.randint(1, no_of_names)
random_payer -= 1

print( f"{names[random_payer]} is going to buy the meal today! ")

