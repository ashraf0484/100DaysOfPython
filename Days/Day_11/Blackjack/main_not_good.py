from random import choice, random
from os import system
# from art import logo

max = 21

def deal_card(hand):
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(choice(deck))
    
def display_computer(uhs, chs):
    print(f"\n\tComputer's Hand: {computer_hand}, Current Score: {computer_hand_sum} ")
    if uhs == max or chs > max:
        print("\n\tYou Win!!!")
        return True
    elif uhs > max or chs == max:
        print("\n\tYou lose!")
        return True

system("clear")
cont = input("Press enter to play Blackjack or any other letter to exit.")

while cont == "":
    system("clear")
    # print(logo)
    #Initializing and randomly chosing hands for both user and computer
    user_hand = []
    computer_hand = []
    game_over = False
    
    for i in range(2):
        deal_card(user_hand)
        deal_card(computer_hand)

    #Initializing sum of both the players
    user_hand_sum = sum(user_hand)
    computer_hand_sum = sum(computer_hand)

    # Printing the users hand and sum
    print(f"\tYour Hand: {user_hand}, Current Score: {user_hand_sum} ")
    print(f"\tComputer's First Card: {computer_hand[0]}")
    game_over = display_computer(user_hand_sum, computer_hand_sum)
        
    pass_or_another_card = input("\nPress enter to get another card or any other letter to pass: ")

    while pass_or_another_card == "" and user_hand_sum < max and not game_over:
        
        deal_card(user_hand)
        user_hand_sum = sum(user_hand)
        print(f"\n\tYour New Hand: {user_hand}, Current Score: {user_hand_sum} ")

        if user_hand_sum > max:
            print(f"\n\tComputer's Hand: {computer_hand}, Current Score: {computer_hand_sum} ")
            print("\n\tYou lose")
            game_over = True
        elif user_hand_sum == max:
            print(f"\n\tComputer's Hand: {computer_hand}, Current Score: {computer_hand_sum} ")
            print("\n\tYou Win!!!")
            game_over = True
        else:
            pass_or_another_card = input("\nPress enter to get another card or any other letter to pass: ")   

    if not game_over:
        computer_pass = (random() < 0.5 )
        while computer_pass and computer_hand_sum < max:
            deal_card(computer_hand)
            computer_hand_sum = sum(computer_hand)
            
            if computer_hand_sum > max:
                print(f"\n\tComputer's Hand: {computer_hand}, Current Score: {computer_hand_sum} ")
                print("\n\tYou Win!!!")
                game_over = True
            elif computer_hand_sum == max:
                print(f"\n\tComputer's Hand: {computer_hand}, Current Score: {computer_hand_sum} ")
                print("\n\tYou lose")
                game_over = True
            else:
                computer_pass = (random() < 0.5 )
    
    if not game_over:        
        print(f"\n\tComputer's Hand: {computer_hand}, Current Score: {computer_hand_sum} ")
        if computer_hand_sum > user_hand_sum:
            print("\n\tYou Lose")
        elif computer_hand_sum == user_hand_sum:
            print("\n\tIt's a draw")
        else:
            print("\n\tYou Win!!!")
        
    cont = input("Press enter to play Blackjack or any other letter to exit.")