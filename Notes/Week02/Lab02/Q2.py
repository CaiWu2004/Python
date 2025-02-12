import random

side = int(input("Will the coin land on 0 (heads) or 1 (Tails)?"))
coin_flip = random.randint(0,1)
print("The coin landed on:", coin_flip)
print("You guessed it correctly:", side == coin_flip)



