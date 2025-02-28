"""
Author: [Harry Wu]
Assignment / Part: HW4 - Q1
Date due: Feb 27, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

#1)

mochiko = int(input("Enter an amount (g) of mochiko: "))
sugar = int(input("Enter an amount (g) of sugar: "))
cornstarch = int(input("Enter an amount (g) of cornstarch: "))
anko = int(input("Enter an amount (g) of anko: "))

"""cup_of_mochiko = int(mochiko // 660)
cup_of_sugar = int(sugar // 330)
cup_of_cornstarch = int(cornstarch // 440)
cup_of_red_bean_paste = int(anko // 220)"""

batch = 0
while mochiko > 660 and sugar > 330 and cornstarch > 440 and anko > 220:
    mochiko -= 660
    sugar -= 330
    cornstarch -= 440
    anko -= 220
    batch += 1

print("With this amount of ingredients, you can make,", batch, "batch(es) of 24 mochi.")





"""mochi = int(cup_of_mochiko + cup_of_sugar + cup_of_cornstarch + cup_of_red_bean_paste)

batch = int(mochi // 24)

print(batch, mochi)"""

