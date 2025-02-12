#Practice:
import math
import random

x = True
y = True
z = False

print((x or y) or (z and z) and z) #True

print((x and y) or (x and y or z) and (4 + 2 * 2 == 24/2)) #True
       # True or True and (16 == 12)  = true or true and false = true and true = true
# do "And" first b/c its like multiplication whereas "or" is like addition

print((x and y) and (6 + 2 * 3 == 20)) # False

print(not(not(8 > 4) or not(y or z) and not(4 == 8/2)))
            #false     or    False    and       False = false or false = not(false) = true


#Use the math module to find the greatest common divisor (GCD) of 24 and 36. Store it in value and print it.
print(math.gcd(24,36))

#Use the random.randint() function to generate two random numbers between 1 and 100, store them in num1 and num2, then print their sum.

num1= random.randint(1,100)
num2 = random.randint(1,100)

print(num1,"+", num2, "=", (num1 + num2))

