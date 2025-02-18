"""
Author: [Harry Wu]
Assignment / Part: HW3 - Q3
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""


xp = float(input("Enter the player's current XP: "))

if xp < 15.0:
    level = 1
    print("Level 1 player","(XP=",xp,")")
elif xp <= 24.9:
    level = 2
    print("Level 2 player","(XP=",xp,")")
elif xp <= 29.9:
    level = 3
    print("Level 3 player","(XP=",xp,")")
elif xp <= 39.9:
    level = 4
    print("Level 4 player","(XP=",xp,")")
elif xp <= 60.0:
    level = 5
    print("Level 5 player","(XP=",xp,")")
else:
    print("Error: Please enter a valid XP value.")
