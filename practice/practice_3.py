#Moduels and Expressions Practice

#1) Fill in the following table with True and False values

"""
print("-----------------------------------------------------------------------------------")
print("p          |q     |(not p)or q | (p and q)or q | (p or q)and p | (p or q) and (p and q)")
print("-----------------------------------------------------------------------------------")
print("True       |True  |  True       | True          | True         | True              ")
print("-----------------------------------------------------------------------------------")
print("True       |False |  False|       False|      True | False ")
print("-----------------------------------------------------------------------------------")
print("False       |True  |  True|True |False|False ")
print("-----------------------------------------------------------------------------------")
print("False      |False | False|False |False|False ")
print("-----------------------------------------------------------------------------------")
"""

#2) Evaluate these expressions
"""
x = True
Y = False
z = False

(x or y) or (z and x) and z   #True or False and False = true and false = false
(x and y) and (6 + 2 * 3 == 20) = false and (6 + 6 == 20) = false and false = false
(8 - 2 > 4) or (x and y or z) and (4 + 2 * 2 == 24/2)     = (true) or (false) and (false) = true and false = false
not(not(8 > 4) or not(y or z) and not(4 == 8/2)) = not(not(true) or not(false) and not(true) = not(false or true and false) = not(true and false) = not(false) = true
"""


#num = 5
# temp = -2
"""
not(num > 0 or temp <= 0) and not(num > 0 and temp <= 0) 
#not(5 > 0 or -2 <= 0) and not(5 > 0 and -2 <=0)
#nnot(true or true) and not(true and true)
#not(true) and not(true)
#false and false
#false

not(not(num > 0 or temp <= 0) or not(num > 0) and temp <= 0) 
#not(not(5 > 0 or -2 <= 0) or not(5 > 0) and -2 <=0)
#not(not(true) or not(true) and true)
#not(false or false and true)
not(false and true)
#not(false) = true
"""

#Modules:

import random,math

"""num = random.randint(1, 10)
print(num)"""

"""rand_float = random.random()
print(rand_float)"""

"""num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
sum = num1 + num2
print(sum)"""

"""even_num = random.randrange(2, 21, 2)
print(even_num)"""

#Math Module:

"""sqrt_25 = math.sqrt(25)
print(sqrt_25)"""

"""floor_val = math.floor(7.9)
print(floor_val)"""

"""gcd_val = math.gcd(24, 36)
print(gcd_val)"""

"""print(round(math.pi, 3))"""

"""power_val = math.pow(2, 5)
print(power_val)"""