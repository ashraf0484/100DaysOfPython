from random import choice 
from os import system
from art import logo
system("Clear")

restart = input("Press enter to play Blackjack or any other letter to exit.")
while restart == "":
    system("Clear")
    print(logo)
    def deal_card():
        """Returns a random card from a standard deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = choice(cards)
        return card

    def calculate_score(cards):  
        """Returns the sum of the passed hand"""
        score = sum(cards)
        if score == 21:
            return 0      
        elif 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
            return score
        else:
            return score
    
    def compare(user_score, computer_score):
        """Pass the scores of the players to compare them and give the desired ouput"""
        print(f"\n\tComputer's Hand: {computer_cards}, Computer's final Score: {computer_score} ")
        if user_score == computer_score:
            print("\nIts a Draw")
        elif computer_score == 0 or user_score > 21:
            print("You Lose")
        elif user_score == 0 or computer_score > 21:
            print("You win")
        elif computer_score > user_score:
            print("You Lose")
        else:
            print("You win")
        
    user_cards = []
    computer_cards = []
    game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n\tYour Hand: {user_cards}, Current Score: {user_score} ")
        # Line 42 is only to be run during the first iteration thats the reason for the line 41
        if len(user_cards) == 2:
            print(f"\tComputer's First Card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or computer_score > 21 or user_score > 21 :
            game_over = True
        else:
            if input("\n\tPress enter to draw another card or any other letter to pass: ") == "" :
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and user_score <21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(user_score, computer_score)

    restart = input("Press enter to play Blackjack or any other letter to exit.")