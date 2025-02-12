"""
Author: [Harry Wu]
Assignment / Part: HW2 - Q1
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""
import math
guest = int(input("How many people are attending?"))
slices = int(input("How many slices of pizza is each guest expected to eat?"))
large_pizza = 8

total_pizza = guest * slices

if total_pizza // 8 == 0:
    mini = total_pizza // 8
else:
    mini = (total_pizza // 8) + 1

left_over = total_pizza % 8



print("Minimum number of whole large pizza required:", mini)
print("Total number of large pizza slices needed:", total_pizza)
print("Number of large pizza slices left over:", left_over)