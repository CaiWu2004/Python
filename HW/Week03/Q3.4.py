"""
Author: [Harry Wu]
Assignment / Part: HW3 - Q4
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

import math

a_value = float(input("Please enter the value of a: "))
b_value = float(input("Please enter the value of b: "))
c_value = float(input("Please enter the value of c: "))

if (a_value == 0):
    if (b_value == 0):
        if (c_value == 0):
            print("Infinity Solution")
        else:
            print("No Solution")
elif (a_value != 0):
    if (b_value == 0):
        if (c_value != 0):
            print("No Real Solution")
else:
    x1 = (-b_value)
