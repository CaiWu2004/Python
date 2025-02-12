''''
#boolean expression
num1, num2= 5,6
state=False
print(not(state or num1 < num2) and num1*num2 == 35)
#not(state or true) and false)
#nnot(true) and false)
#false and false = false
'''
#selection statment
'''
if
    if ....else
    if elif...else'''

#one way selection if statment
"""""
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")# if condition is true
    print("Enjoy your rights!")
    age = age + 5
    print("Your age is now", age)

print("This is not the year for you to vote!") """""

#two way selection statment: if ... else
"""""
if age >= 18:
    print("You can vote!")# if condition is true
    print("Enjoy your rights!")
    age = age + 5
    print("Your age is now", age)
else:
    print("Sorry, you can't vote! You have rights only at certain age.")
    #execute if condition is false


print("This is not the year for you to vote!")"""""

#if ... elif

#Conditional Statment
''''
if temperature > 0:
    status = "above freezing"
else:
    status = "below freezing"


print(item_count, 'item' if item_count == 1 else 'items') '''

'''''
#Conditional Expression Problems 2

num = float(input("Enter a number: "))

sign = "positive" if num > 0 else "negative"

print(sign)
'''
'''''
#Conditional Expression Problems

day = input("Enter today's day of the week: ")

day_type = "weekend" if day == "Saturday" or day == "Sunday" else "weekday"
print("Today is a", day_type)
'''
'''''
score = float(input("Enter your test score: "))

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >=  70:
    letter = "C"
elif score >= 60:
    letter = "D"
else
    letter = "F"

print("your score of", score, "gets you the letteer)")
'''
'''''
#Nested if statements

age = int(input("Enter your age: "))
have_id = input("Have ID? T/F")

if age >= 18:
    print("You are an adult!")
    have_id = input("Have ID? T/F")
    if have_id.upper() == "T" or have_id.upper()== "TRUE":
        print("You can enter!")
    else:
        print("You shell not pass!")
else:
    print("Your are a fucking minor!No entry allow!")
'''
''''
#6: Even Odd:

number = float(input("Enter a number: "))
message = ""

if number > 0:
    message += "Positive"
    if number % 2 == 0:
        message += "Even"
    else:
        message += " and Odd"
elif number < 0:
    message += "negative"
    if number % 2 == 0:
        message += "even"
    else:
        message += " and Odd"
else:
     message ="Zero"

print(number, "is", message)'''\

"""
student = input("Are you a student? T/F")

if student == "T":
    print("$10")
else:
    age = int(input("Enter your age: "))
    if age < 18:
        print("15")
    else:
        print("20")"""

score = float(input("Enter your test score: "))

"""if score < 90:
    if score < 80:
        if score < 70:
            if score < 60:
                print("F")
            else:
                print("D")
        else:
            print("C")
    else:
        print("B")
else:
    print("A")"""

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


