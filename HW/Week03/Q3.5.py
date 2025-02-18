"""
Author: [Harry Wu]
Assignment / Part: HW3 - Q5
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

import math
import random

hp_max = int(input("What is the maximum health point of the pokemon?"))
hp_current = int(input("What is the current health point of the pokemon?"))
ball = random.randint(0, 255)
catch_rate = random.randint(0, 255)

f = round((hp_max * 255 * 4)/ (hp_current * ball))

if f >= catch_rate:
    print("Pokemon caught!")
else:
    print("Oh no! The pokemon broke free!")

