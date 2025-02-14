import random


dealer_card_sum = random.randrange(2, 22)
player_card_sum = random.randrange(1, 12)

print("Welcome to Blackjack!")
print("Your current card sum is:", player_card_sum, "and the dealer has:", dealer_card_sum)
choice = print("What would you like to do?: (DEAL, STAND" )
while choice == "DEAL" and player_card_sum < 21:
    new_card = random.randrange(1, 12)
    player_card_sum += new_card
    print("Your current card sum is:", player_card_sum, "and the dealer has:", dealer_card_sum)
    choice = print("What would you like to do?: (DEAL, STAND")
if player_card_sum > 21:
    print("You lost! Your card sum is:", player_card_sum, "and the dealer has:", dealer_card_sum)
elif player_card_sum == dealer_card_sum:
    print("Its a tie")
elif player_card_sum > dealer_card_sum:
    print("You win! Your card sum is:", player_card_sum, "and the dealer has:", dealer_card_sum)
else:
    print("You lose!")


