import random

print("Hello! Welcome to the Doctor's office!")

month = random.randrange(9, 12)
day = random.randrange(3, 31, 3)

if month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"

print("Your doctos appointment is scheduled for", month, day,"! Have a great day!")
