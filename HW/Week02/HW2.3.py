"""
Author: [Harry Wu]
Assignment / Part: HW2 - Q3
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

import random
import math

random_integer = random.randint(1, 20)
print("Random integer(1-20):", random_integer)
square_root = round(math.sqrt(random_integer), 2)

print("Square root of", random_integer, "is:", square_root)

area = round((math.pi * (square_root ** 2)), 2)

print("Area of circle with radius", square_root, "is:", area)