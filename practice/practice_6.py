#Nested if statement practice problems

#1) Age Classification:

"""age = int(input("Plase enter your age: "))
if age < 20:
    if age >= 13:
        print("Teenager")
    elif age >= 0:
        print("Child")
else:
    print("Adult")"""

#2) Grade Evaluation:

"""score = int(input("Please enter your score(0-100): "))
if score >= 60:
    if score < 70:
        print("D")
    elif score < 80:
        print("Needs Improvement")
        print("C")
    elif score < 90:
        print("Good")
        print("B")
    elif score < 100:
        print("Excellent")
        print("A")
else:
    print("F")"""

#3) Password Validator:

"""username = str(input("Please enter your username: "))
password = int(input("Please enter your password: "))

if username == "admin":
    if password == 1234:
        print("Correct password and username.")
    else:
        print("Incorrect password. Please try again")
else:
    print("Invalid username. Please try again.")"""

#4) Shopping Discount:

"""
total_amount = int(input("What is your total purchase amount?: "))
discount_code = str(input("Do you have a discount code? (Y/N): "))


if total_amount > 100:
    if discount_code == 'Y':
        new_amount = total_amount - (total_amount * 20/100)
        print("Your total amount is: ", new_amount)
    else:
        new_amount = total_amount - (total_amount * 10/100)
        print("Your total amount is: ", new_amount)
else:
    print("Your total is less than $100, so there is no discount.")
"""

#5) Temperature Checker:

"""
temperture = int(input("Please enter your temperature: "))

if temperture > 0:
    if temperture > 30 and temperture > 20:
        print("Hot")
    else:
        print("Cold")
else:
    print("Freezing")
"""

#6) Even or Odd:

"""num = int(input("Please enter your number: "))

if num == 0:
    print("The number is zero.")
elif num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif num < 0:
    print("The number is negative.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")"""

#7) Loan Eligibility:

"""income = int(input("Please enter your income: "))
credit_score = int(input("Please enter your credit score: "))

if income > 50000:
    if credit_score > 700:
        print("Eligible for loan.")
    else:
        print("Not eligible for loan.")
else:
    print("Not eligible for loan.")
"""
#8)

"""fitness_level = str(input('What fitness level do you want to start with(beginner, intermediate, advance)? '))

if fitness_level != 'beginner':
    if fitness_level == 'intermediate':
        print("Weight Training")
    elif fitness_level == 'advance':
        print("Crossfit")
else:
    print("Yoga")"""

#9)

"""age = int(input("Please enter your age: "))

if age < 20:
    if age >= 13:
        print("You're a teenager, you have to pay $10.")
    else:
        print("Children enter for free.")
else:
    print("As an adult you have to pay $20.")"""

#10) Correct Ticket Pricing:

"""age = int(input("Please enter your age: "))
student = str(input("Are you a student(Y/N): "))

if student == 'N':
    if age < 18:
        print("Ticket price is $15")
    else:
        print("Ticket price is $20")
else:
    print("Ticket Price is $10")"""














