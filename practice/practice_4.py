#Python Modules Practice (math, random)

#1) Random Number Generation

import math, random

"""rand_num = random.randint(1, 100)
print(rand_num)

if rand_num >= 50:
    print("This number is greater than or equal to 50")
else:
    print("This number is less than or equal to 50")"""

#2) Square Root Calculation:

"""num = int(input("Enter a number: "))

sqrt = math.sqrt(num)
print(sqrt)
if sqrt > 5:
    print("This number is greater than 5")
else:
    print("This number is less than or equal to 5")"""

#3) Random Float Comparison:

"""float_comp = random.uniform(0, 10)
print(float_comp)
if float_comp < 7.5:
    print("This number is less than 7.5")
else:
    print("This number is greater than 7.5")"""

#4) Exponential Check:

"""num = int(input("Enter a number: "))
print(math.exp(num))"""

#5) Random Number Range Check:

"""num1 = random.randint(1, 50)
num2 = random.randint(1, 50)

if num1 < num2:
    print("The first number is smaller than the second number")
else:
    print("The first number is not smaller than the second number")"""


#6) Logarithm Comparison:

"""num = float(input("Enter a positive number: "))

while num < 0:
    float(input("The input is negative. Thus invalid. Please enter a positive number: :"))
    num = float(input("Enter a positive number: "))
log_of_ten = math.log10(num)
if log_of_ten > 1:
    print(f"{log_of_ten} is greater than 1")
else:
    print(f"{log_of_ten} is less than 1")"""


#7) Random Integer Modulo:

"""num = random.randrange(1,20)
remainder = num % 4
if remainder == 2:
    print(f"The remainder of {num} is equal to 2.")
else:
    print(f"The remainder of {num} is {remainder}.")
"""
#8) Power Calculation:

"""num = int(input("Enter a number: "))

result = math.pow(num, 3)

if result > 100:
    print(f"The result of {num} is greater than 100.")"""

#9) Random Even Number Check:

"""rand_num = random.randint(1, 50)
if rand_num % 2 == 0:
    print(f"The random number, {rand_num} is an even number.")
else:
    print(f"The random number, {rand_num} is an odd number.")"""

#10) Trigonometric Function Comparison:

"""degrees = float(input("Enter a number: "))
rad_num = math.radians(degrees)
sine_value = math.sin(rad_num)

if sine_value > 0.5:
    print("The sine value is greater than 0.5.")
else:
    print("The since value is less than 0.5.")"""

#11) Random Angle and Sine Comparison:

"""angle = random.randint(0, 360)
angle_rad = math.radians(angle)
sine_value = math.sin(angle_rad)
print(f"The sine is {sine_value}")
if sine_value > 0.5:
    print("The sine value is greater than 0.5.")
else:
    print("The sine value is less than 0.5.")"""

#12) Random Integer and Square Root:

"""num = random.randint(1, 100)
sqrt_val = math.sqrt(num)
print(f"The sqrt of {num} is {sqrt_val}")
if sqrt_val < 10:
    print(f"{sqrt_val} is less than 10")
"""

#13) Logarithm of Random Integer:

"""num = random.randint(10, 100)
log_of_ten = math.log10(num)
if log_of_ten > 2:
    print(f"{log_of_ten} is greater than 2")
else:
    print(f"{log_of_ten} is less than 2")"""

#14) Power of Random Float:

"""random_float = random.uniform(0,5)
power = math.pow(random_float,3)
if power > 50:
    print(f"The result of {random_float} to the power of 3 is {power} which is greater than 50.")
else:
    print("It's not greater than 50.")"""

#15) Random Number and Exponential Comparison:

"""num = random.randint(1,20)
exponental_num = math.exp(num)
if exponental_num < 1000:
    print(f"{exponental_num} is less than 1000")
else:
    print(f"{exponental_num} is greater than 1000")"""

