"""
Author: [Harry Wu]
Assignment / Part: HW1 - Q3
Date due: January 30, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

print("Please input how much money you have base on the number of coins!")

quarter = int(input("Quarter: "))
dime = int(input("Dime: "))
nickel = int(input("Nickel: "))
penny = int(input("Penny: "))

total = int(quarter * (25)) + int(dime * (10)) + int(nickel * (5)) + int(penny * (1))

dollar = total // 100
cents = total % 100
#the % represents the remainder
#// means to divide
print("You have",dollar,"dollars and",cents,"cents!")