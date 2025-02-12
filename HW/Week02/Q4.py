"""
Author: [Harry Wu]
Assignment / Part: HW2 - Q4
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

import math

days_summant = int(input("Enter the number of days Summant has worked:"))
hours_summant = int(input("Enter the number of hours Summant has worked:"))
minutes_summant = int(input("Enter the number of minutes Summant has worked:"))
days_sarah = int(input("Enter the number of days Sarah has worked:"))
hours_sarah = int(input("Enter the number of hours Sarah has worked:"))
minutes_sarah = int(input("Enter the number of minutes Sarah has worked:"))

total_days = days_summant + days_sarah
total_hours = hours_summant + hours_sarah
total_minutes = minutes_summant + minutes_sarah

total = (total_days * 24 * 60) + (total_hours * 60) + total_minutes

days = total // (24 * 60 )

total -= days * (24 * 60 )

hours = total // (60)

total -= hours * (60)

minutes = total


print("The total time both CAs worked togther is:", days, "days,", hours, "hours,", minutes, "minutes.")
