"""
Author: [Harry Wu]
Assignment / Part: HW4 - Q3
Date due: Feb 27, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

#3) Baby Steps

days = int(input("Enter number of days (1 to 100): "))
total = 0

while days < 1 or days > 100:
    days = int(input("Enter a valid number of days (1 to 100): "))

for steps in range(1, (2 * days), 2):
    total += steps

print("The baby will have taken a total of", total, "steps after",days,"days.")

"""total = 0
steps = 1
for _ in range(1, days+1):
    total += steps
    steps += 2"""







"""
if days < 0:
    input("Enter a valid number of days (1 to 100): ")
elif days > 100:
    input("Enter a valid number of days (1 to 100): ")
else:
    print(days)"""

"""for days in range(1, days + 1):
    for steps in range(1, days + 1):
        steps += 2
    print("One the ")"""

