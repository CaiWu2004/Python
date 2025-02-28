"""
Author: [Harry Wu]
Assignment / Part: HW4 - Q2
Date due: Feb 27, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

#2) Must be funny in the rich man's world

players = int(input("How many players played this round? "))
while players <= 0:
     players = int(input("Invalid input. How many players played this round? "))

for i in range(0, players):
    bank = 0
    asset = input("Enter the value of property/asset, or Done to finish: ")
    while asset != "DONE":
        bank += float(asset)
        asset = input("Enter the value of property/asset, or Done to finish: ")
    text = 'Player {} has ${:.2f} bank assets.'
    print(text.format(players-2, bank))
    players += 1















"""average = (num1 + num2 + num3)/3
#average = round(average,6)
print(f"{average:.6f}")"""

"""interest_rate = 20
balance = float(input("What is the user's account balance (a float)? "))
result = balance*(1 + (interest_rate/100))
text = "With interest, the new account balance is: ${num:.2f}"
print(text.format(num=result))
"""