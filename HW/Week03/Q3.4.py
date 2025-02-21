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
my_discriminant = (math.sqrt(b_value ** 2 - 4 * a_value * c_value))

if (a_value == 0):
    if (b_value == 0) and (c_value == 0):
        print("The Question has Infinity Solution")
    else:
        print("No Solution")
elif my_discriminant == 0:
    x1 = ((-b_value) + (math.sqrt(b_value ** 2 - 4 * a_value * c_value))) / (2 * a_value) #x1 = -b/2a
    print("This equation has 1 solution: x=", x1)
elif my_discriminant > 0:
    x1 = ((-b_value) + (math.sqrt(b_value ** 2 - 4 * a_value * c_value))) / (2 * a_value)
    x2 = ((-b_value) - (math.sqrt(b_value ** 2 - 4 * a_value * c_value))) / (2 * a_value)
    print("This equation has 2 solutions: x1=", x1, "x2=", x2)
else:
    print("This equation has no real solutions")





