from random import randint 
import os
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]

round = int(input("\n\n\nHi\nWelcome to Rock, Paper, Scissors\nHow many rounds do you wanna play? : "))
i = 1
score = 0

while i <= round:
        
    print(''' 
0 - Rock
1 - Paper
2 - Scissors             
''')
    
    
    user = int(input("Enter your option: "))
    
    if user >= 3 or user < 0:
        print("Invalid input!\n")
        input("\nPress any key to continue")
        os.system('clear')
        continue
    
    print(f"You chose {image[user]} ")
    
    computer = randint(0,2)
    print(f"\nComputer chose {image[computer]}\n")   
    
    
    if user == computer:
        print("It's a draw!\n")
    elif computer == 0 and user == 2:
        print("You lose\n")
    elif user == 0 and computer ==2:
        print("You win\n")
        score += 1
    elif computer > user:
        print("You lose\n")
    else:
        print("You win\n") 
        score += 1  
        
    input("\nPress any key to continue")
    os.system('clear')
             
    i += 1


print(f"Your score is {score} ")
if score > (round/2):
    print("\nYou won the entire game\nWOWWWW!!\n\n\n")
elif score == (round/2):
    print("\nIts draw!")
else:
    print("\nDAAANG... YOu aRe A HugE LoSeR\n\n\n")