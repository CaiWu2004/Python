"""Arithmetic Operations"""
"""1)Write a Python program that takes two numbers as 
input and performs all the basic arithmetic operations 
(addition, subtraction, 
multiplication, division, floor division, modulus, exponentiation). """

"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1, "+", num2, "=", num1 + num2)
print(num2, "-" ,num1, "=", num2 - num1)
print(num1, "*", num2, "=", num1 * num2)
print(num2, "/", num1, "=", num2 / num1)
print(num2, "//", num1, "=", num2 // num1)
print(num2, "%", num1, "=", num2 % num1)
print(num1, "**", num2, "=", num1 ** num2)"""

"""2) Create a program that calculates the 
area of a rectangle given its length and width."""

"""length = int(input("Enter the length of the rectangle(inch): "))
width = int(input("Enter the width of the rectangle(inch): "))

area_of_rectangle = length * width

print("The area of the rectangle is", area_of_rectangle, "inch square.")"""

"""Comparison and Logical Operators"""

"""1) Write a Python program that compares two given numbers and prints whether they are 
equal, greater, or less than each other."""

"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
 print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)"""

"""2) Implement a program that checks if a given number is even and greater than 10."""

"""num1 = int(input("Enter a number: "))
if num1 >= 10:
    print(num1, "is greater than or equal to 10 and is even.")
else:
    print(num1, "is less than 10")"""

"""Assignment Operations:"""

"""1) Create a program 
that uses assignment operators to 
update a variable's value based on user input."""

"""num2 = int(input("Enter a number: "))
num = 0
num += num + num2
print("The value of the number is:",num)"""

"""2) Create a program that increments a variable’s value by 2 each time it is updated."""

"""num2 = int(input("Enter a number: "))
num = 0
num += num + num2
print("The value of the number is:",num)
num += 2
num += num + num2
print("The value of the number is:",num)"""

"""Booloean Practice:"""

"""1) Write a Python program that checks if a user-inputted number is positive."""

"""num = int(input("Enter a number: "))
print(num > 0)"""

"""2) Implement a program that checks if a given year is a leap year."""

"""year = int(input("Enter the year: "))
print(year % 4 == 0)"""

"""Expression Challenges"""

"""1) Create a program that calculates the 
volume of a cylinder given its radius and height."""
import math
"""radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))

volumn = math.pi * ((radius**2 ) * height)
print(volumn)"""

"""2) Implement a program that 
converts temperature from Celsius to 
Fahrenheit using the formula: `F = (C * 9/5) + 32`."""

"""celsius = int(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", fahrenheit)"""


"""3) Write a Python program that calculates 
the hypotenuse of a right-angled triangle using the Pythagorean theorem."""

"""import math

opposite = int(input("Enter angle oppisite to the hypothenuse of the right-triangle: "))
adjcent = int(input("Enter angle adjcent to the hypothenuse of the right-triangle: "))

hypothenuse = math.sqrt(adjcent ** 2 + opposite ** 2)
print(hypothenuse)"""

#Mixed Problems:

#1)
"""
Write a program that checks if a given year 
is a leap year and if a number is divisible by both 3 and 5.
"""

"""def leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def check_divisible(num):

    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False

print(leap_year(2020))
print(check_divisible(2020))


year = int(input("Enter the year: "))
leap_year= year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(leap_year)

num = int(input("Enter a number: "))
divisable = num % 3 == 0 and num % 5 == 0
print(divisable)"""

#2)
"""
Create a simple calculator program that takes two numbers and an 
operation (+, -, *, /) as input and performs the calculation.
"""

"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operation(+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)"""
