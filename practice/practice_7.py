# While Loop Practice:

#1) User Input Validation:

"""integer = int(input("Please enter a positive number: "))

while integer < 0:
    integer = int(input("Invalid input.Please enter a positive number: "))
"""

#2) Countdown until zero:

"""
num = int(input("Please enter a positive number: "))

while num >= 0:
    print(num)
    num -= 1
"""

#3) Sum of Positive Numbers:
"""
total = 0
num = int(input("Please enter a number(positive to continue and negative to stop): "))
total = total + num
print(total)
while num > 0:
    num = int(input("Please enter a number(positive to continue and negative to stop): "))
    if num > 0:
        total += num
        print(total)
print("The total is",total)
"""

#4) Temperature Conversion:

"""temp = int(input("Please enter a temperture in celsius(-10 to quite): "))
fahrenheit =(temp * (9/5)) + 32
print(fahrenheit)
while temp != -10:
    temp = int(input("Please enter a temperature in celsius(-10 to quite): "))
    fahrenheit = (temp * (9/5)) + 32
    print(fahrenheit)"""

#5) Finding Factorial
"""import math
num = int(input("Please enter a positive number: "))

while num < 0:
    num = int(input("Invalid number.Please enter a positive number: "))
    if num > 0:
        fact = math.factorial(num)
        print(f"The factorial of {num} is {fact}.")"""

#6) Even or Odd Counter
"""even = 0
odd = 0
num = -1

while num != 'Done':
    num = str(input("Please enter a positive number(Enter 'Done' to end): "))
    if num != 'Done':
        num = int(num)
        if num % 2 == 0:
            even += 1
        elif num % 2 == 1:
            odd += 1
print(even,"even and", odd,"odd.")"""

#7) Repeated String Concatenation:

"""phrase = " "
words = " "
while phrase != 'stop':
    phrase = str(input("Please enter a string: "))
    words = words+" "+phrase
    print(words)"""

#8) Cumulative Average Calculation:


total = 0
count = 0
num = int(input("Please enter a positive number: "))

while num >= 0:
    total += num
    count += 1
    num = int(input("Please enter a positive number(negative int to stop): "))
average = total/count
print(average)

# total = 0
# count = 0
# num = int(input("Please enter a positive number: "))
# total += num
# count += 1
# print(total)
# while True:
#     num = int(input("Please enter a positive number(negative int to stop): "))
#     if num > 0:
#         total += num
#         count += 1
#     # print(total)
#     if num < 0:
#         break
# average = total/count
# print(average)




"""total = 0
count = 0
num = -1
while num > 0:
    if num >= 0:
        num = int(input("Please enter a positive number: "))
        total += num
        count += 1
        print(total)
    elif num < 0:
        average = total/count
        print(average)"""

#9) Guessing Game with a limit

"""import random

guess = 5
guess_answer = -1
num = random.randint(1,100)
print(num)
while guess_answer != num and guess > 0:
    guess_answer = int(input("Please guess the number: "))
    guess -= 1
    if guess == 0 and guess_answer != num:
        print("You used up all your guesses!")
    elif guess_answer == num:
        print("You guessed the number!")"""

#10) ATM Withdrawal Simulation:

import random

funds = random.randint(1,10000)
withdraw = int(input("PLease enter the withdraw amount:"))

while funds < withdraw:
    withdraw = int(input("PLease enter the withdraw amount:"))

print("success, you can withraw", withdraw, "from", funds)












