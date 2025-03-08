"""
Author: [Harry Wu]
Assignment / Part: HW5 - Q2
Date due: Mar 6, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

num = int(input("Enter a positive integer 'max_num': "))
print("A")
pattern = "A"

for i in range(2, num + 1):
    new_pattern = ""
    for char in pattern:
        if char == "A":
            new_pattern += "B"
        elif char == "B":
            new_pattern += "A"
    pattern += new_pattern
    print(pattern)

#it starts at "A" then prints A and since its A new_pattern becomes B and is added to pattern making it AB
#then it checks A from AB and add B to AB making it ABB, it then checks B and turn it into A and added to ABB making it ABBA
# This keeps on happening unto you get a patter
