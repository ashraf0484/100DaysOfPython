from game_data import data
from art import logo, vs
from random import choice, randint
from os import system

def printer(var, name):
    print(f"Compare {name}: ", end="")
    print(data[var]["name"], end=", a ")
    print(data[var]["description"], end=", from ")
    print(data[var]["country"], end=".")

len_data = len(data)

a = randint(0, len_data-1)
b = randint(0, len_data-1)
# Not to repeat the same persons
while b == a:
    b = randint(0, len_data-1)

score = 0
cont = True

while cont :

    system("clear")
    print(logo)

    if score > 0:
        print(f"You are right!, you're score is {score}")

    printer(a, "A")
    print(vs)
    printer(b, "B")
    
    choice = input("\nWho has more Instagram Followers? 'A' or 'B': ").lower()

    if data[a]["follower_count"] > data[b]["follower_count"] and choice == 'b':
        cont = False
    elif data[b]["follower_count"] > data[a]["follower_count"] and choice == 'a':
        cont = False
    else:
        score += 1
    
    a = b
    while b == a:
        b = randint(0, len_data-1)

print(f"Your final score is {score}")
