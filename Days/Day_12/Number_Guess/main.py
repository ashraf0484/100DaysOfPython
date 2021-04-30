from random import randint
from os import system
number = randint(1, 100)
easy = 10
hard = 5

def game(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess > number and attempts == 1:
            print("Too high.")
            print("You've run out of guesses, you lose.")
        elif guess < number and attempts == 1:
            print("Too low.")
            print("You've run out of guesses, you lose.")
        elif guess > number :
            print("Too high.")    
            print("Gueess again.")
        elif guess < number :
            print("Too low.")    
            print("Gueess again.")
        else :
            print(f"You got it! The answer was {number}")
            exit()
        attempts -=1   
system("clear")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\": ").lower()

if difficulty == "easy":
    game(easy)
elif difficulty == "hard":
    game(hard)


