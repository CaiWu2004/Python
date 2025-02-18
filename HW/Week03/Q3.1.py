"""
Author: [Harry Wu]
Assignment / Part: HW3 - Q1
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

print("Welcome to the lemonade Stand Profit Calculator!")
season = input("Enter the current season (summer/other):" )
small_cups = int(input("Enter the number of small cups of lemonade sold:"))
medium_cups = int(input("Enter the number of medium cups of lemonade sold:"))
large_cups = int(input("Enter the number of large cups of lemonade sold:"))

if season == "summer":
    small_profit = float(2.00)
    medium_profit = float(2.50)
    large_profit = float(3.00)
    small_cost = float(1.00)
    medium_cost = float(1.25)
    large_cost = float(1.50)
elif season == "other":
    small_profit = float(1.75)
    medium_profit = float(2.25)
    large_profit = float(2.75)
    small_cost = float(0.75)
    medium_cost = float(1.00)
    large_cost = float(1.25)
else:
    ()

total_profit = (small_cups * (small_profit - small_cost)) + (medium_cups * (medium_profit - medium_cost)) + (large_cups * (large_profit - large_cost))

print("Total profit for the day is:", total_profit)

