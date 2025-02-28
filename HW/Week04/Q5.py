"""
Author: [Harry Wu]
Assignment / Part: HW4 - Q5
Date due: Feb 27, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

star = int(input("Enter a number: "))

for row in range(0, star - 1):
    for col in range(0, row):
        print(" ", end="")
    for column in range((star-row-1)*2+1):
    #for column in range((star- 1)*2 - (row)*2-1): # 7, 6, 5 ,4
        # 7 5 3 1
        print("*", end="")
    print()
for row in range(star):
    for col in range(star - row - 1):
        print(" ", end="")
    for column in range(2 * row + 1):
        print("*", end="")
    print()



