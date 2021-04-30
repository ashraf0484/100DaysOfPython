#Step 1 
from random import *
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = choice(word_list)

guess = input("Enter your guess: ").lower()

for letter in chosen_word:
    if guess == letter:
        print ("True")
    else:
        print ("False")