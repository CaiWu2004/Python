#This is for arithmitic/math operators
# (), ^, *, /, +, -
num1 = 5
num2 = 15

#expression

result = num1 + num2 / 3 #result = 10
print(result)

result= num1 // 3 # result = 1 b/c it rounds down
result = num1 ** 2 # result = 25

#comparision operators
#: >, <, >==, ,<==, ==, !=(evaluate to true or false)

print(num1 > num2)

print(num1 == num2)

print(num1 == 5)

print(num2 - num1 > 6) # True

# Logical Operators: and, or, not

print(True and False) # False

# T and F = F, F and F = F, F and T = F, T and T = T
# T or F = T, F or T = T, T or T = T, F or F = F

print(True and not False) # True

# math module
import math
import random
from math import sqrt, pow, floor, pi #these are the only things we need to import
num1 = 5
num2 = 15

#print(math.sqrt(num1))
#print(math.pow(num1, 2))
print(pow(num1, 2))
print(sqrt(num1))
print(math.pi)

#random module

print(random.randint(1, 1000))
print(random.random())
print(random.randrange(1,10,2))

# math module

num1 = 5
num2 = 15

print(math.sqrt(num1))

#Generate a random even number between 2 and 20 using the random module.
# Store it in a variable called even_num and print it.

even_num = random.randrange(2,20,2)
print(even_num)

