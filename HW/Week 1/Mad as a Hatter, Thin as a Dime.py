"""
Author: [Harry Wu]
Assignment / Part: HW1 - Q4
Date due: January 30, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""



dollars = int(input("Enter amount of dollars:"))
cents = int(input("Enter amount of cents:"))

total = (dollars * 100) + cents

quarters = total // 25

total -= quarters * 25

dimes = total // 10

total -= dimes * 10

nickels = total // 5

total -= nickels * 5

pennies = total // 1

total -= pennies * 1

print("You have", quarters, "quarters,", dimes, "dimes", nickels, "nickels", pennies, "pennies")

