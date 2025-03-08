# Custome Exponentiation Function:

"""
-Problem: Write a function called power(base, exp) that
computes the power of a base raised to an exponent
without using the ** operator or built-in functions.
- Challenge: Handle both positive and negative exponents.
For example, power(2, 3) should return 8, and power(2,-3) should
return 0.125.
"""
import math

"""def power(base, exp):
   if exp < 0:
       base = 1/base
       exp = -exp

   result = 1

   for _ in range(exp):
       result *= base

   return result

print(power(2, -3))"""
#factorial
"""def factorial(n):
    if n == 0:
        return 1

    result = 1

    for num in range(2, n+1):
        result *= num

    return result

print(factorial(11))"""
#fibonacci
"""def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

print(fibonacci(10))"""

"""def greatest_common_divisor(a,b):
    #continue the proccess until b becomes 0
    while b != 0:
        # apply the Euclidean algorithm
        a, b = b, a % b # Update a to b, and b to a % b

    return a # when b becomes 0, a is the GCD



print(greatest_common_divisor(48,18))"""

"""
For greatest_common_divisor(48, 18):

48 % 18 = 12, so the new pair becomes 18, 12.
18 % 12 = 6, so the new pair becomes 12, 6.
12 % 6 = 0, so the GCD is 6.

This solution efficiently handles both small and 
large values of a and b. 
Let me know if you need further clarification or help!
"""

"""
Write a function called is_prime(n) that checks whether a 
given non-negative integer n is a prime number.

Challenge:
Handle both small and large values of n efficiently. 
A prime number is a number greater than 1 that has 
no positive divisors other than 1 and itself.

For example:

is_prime(5) should return True (because 5 is prime).
is_prime(4) should return False (because 4 is divisible by 2).
Hint:
To check if a number n is prime:

If n <= 1, it is not prime.
Check divisibility for all numbers from 2 to the square root of n.
If n is divisible by any of these numbers, it is not prime.
"""

"""
#My solution
def is_prime(n):
    if n < 1:
        return False

    if n % 1 == 0 and n % 2 != 0:
        return True
    else:
        return False

print(is_prime(3**2))
"""
"""
import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False # n is divisible by i, so it's not prime

    return True # n is prime if no divisor were found

print(is_prime(25))
"""

"""def sum_of_divisors(n):
    if n <= 1:
        return 0

    divisors = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors += i

            if i != 1 and i != n // i:
                divisors += n // i
    return divisors

print(sum_of_divisors(28))
"""

#3. Custom String reversal Function:

"""
Problem: Write a function reverse_string(s) 
that takes a string as input and returns the string reversed.
"""

"""def reverse_string(s):
    return s[::-1]
print(reverse_string("Happy Birthday!"))"""

#4. Impementing a Simple Calculator:

"""
Problem: Create a function calculator(num1, num2, operator) 
that takes two numbers and an operator (+,-, *, /) 
as arguments and performs the specified operation.
Challenge: Handle division by zero gracefully 
and return an error message.
"""

"""def calculator(num1, num2, operator):
    if num2 == 0:
        return "error"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

print(calculator(1, 0, "+"))"""

#5. Counting Vowels in a string

"""def count_vowels(s):
        vowels = 0
        s.lower()
        for char in s:
            if char in "aeiou":
                vowels += 1
        return vowels
print(count_vowels("Harry Wu"))"""

#6. Converting Decimal to Binary

#7. Simple Interest Calculator:

"""def calculate_simple_inteest(principal, rate, time):
    return (principal * rate * time) / 100

print(calculate_simple_inteest(5000, 7, 3))"""

#8. String Compression:

def compress_string(s="ddaannccee"):
    num = 0
    char = ""
    for index in range(0, len(s)):
       if char in s[index] == s[index - 1]:
           num += 1
       print(s[index], num, end=" ")
    return num

print(compress_string("ddaannccee"))

#9. Custome Encryption:

def encrypt_message(message, key):
    message =