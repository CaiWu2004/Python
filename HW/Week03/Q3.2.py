"""
Author: [Harry Wu]
Assignment / Part: HW3 - Q2
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""



day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = float(input("Enter the duration of the call (in minutes): "))

if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thur":
    if time > 530 and time < 2100:
        rate = duration * 0.55
    elif time < 530 and time > 2100:
        rate = duration * 0.35
elif day == "Fri" or day == "Sat" or day == "Sun":
    rate = duration * 0.10

float(print("This call will cost: $", rate))


