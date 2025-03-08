"""
Author: [Harry Wu]
Assignment / Part: HW4 - Q4
Date due: Feb 27, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""
import random

play = input("Would you like to play 'twenty-One'? [y/n] ")

while not (play == 'y' or play == 'n'):
    play = input("Would you like to play 'twenty-One'? [y/n] ")

if play == 'y':
    cards = 0
    player_card_1 = random.randint(1,11)
    player_card_2 = random.randint(1,11)
    opponent_cards = random.randint(0,100)
    while opponent_cards < 3 or opponent_cards > 33:
        opponent_cards = random.randint(0,100)
    print("Your cards are worth",player_card_1,"and",str(player_card_2) + ".")
    cards += player_card_1 + player_card_2
    draw = input("Would you like another card? [y/n] ")

    while not (draw == 'y' or draw == 'n'):
        draw = input("Would you like another card? [y/n] ")
    if draw == 'y':
        cards += random.randint(1,11)
    print("Your score is", str(cards) + "!")
    print("Your opponents score is", str(opponent_cards)+"!")

    if (cards > opponent_cards and cards <= 21) or (opponent_cards > 21 and cards <= 21): # if (cards > opponent_cards or opponent_cards > 21) and cards <= 21:
        print("You Win! Your score was ", str(cards)+".")
    elif (cards < opponent_cards and opponent_cards <= 21) or (opponent_cards <= 21 and cards > 21):
        print("Your opponent wins! Their score was", str(opponent_cards )+".")
    #elif opponent_cards > 21 and cards <= 21:
        #print("You win!")
    #elif opponent_cards <= 21 and cards > 21:
        #print("You Lose!")
    else:
        print("Its a draw!")
else:
    print("Thank you for playing!")

