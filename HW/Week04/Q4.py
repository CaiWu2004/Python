"""
Author: [Harry Wu]
Assignment / Part: HW4 - Q4
Date due: Feb 27, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""
import random

play = input("Would you like to play 'twenty-One'? [y/n] ")

while play != 'y':
    print("Thank you for playing!")
    play = input("Would you like to play 'twenty-One'? [y/n] ")
if play == 'y':
    cards = 0
    player_card_1 = random.randint(1,11)
    player_card_2 = random.randint(1,11)
    opponent_cards = random.randint(0,100)
    while opponent_cards < 3 and opponent_cards > 33:
        opponent_cards = random.randint(0,100)
    print("Your cards are worth", player_card_1, "and", player_card_2,".")
    cards += player_card_1 + player_card_2
    draw = input("Would you like another card? [y/n] ")
    if draw == 'y':
        cards += random.randint(1,11)
    print("Your score is", cards,"!")
    print("Your opponents score is", opponent_cards, "!")

    if cards > opponent_cards and cards < 21:
        print("You win! Your score was ", cards,".")
        if cards == 21 and opponent_cards != 21:
            print("You Win! Your score was ", cards,".")
        else:
            print("Your opponent wins! Their score was",opponent_cards,".")
    elif cards < opponent_cards and cards < 21:
        print("Your opponent wins! Their score was", opponent_cards,".")
    else:
        print("Its a draw!")

