"""
Author: [Harry Wu]
Assignment / Part: HW5 - Q1
Date due: Mar 6, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

initals = input("Enter the initials of the suspects: ")
candy_wrappers = input("Enter the candy wrappers: ")

for i in range(len(candy_wrappers)):
    if candy_wrappers[i] in initals:
        print(candy_wrappers[i], "is a candy thief suspect")

