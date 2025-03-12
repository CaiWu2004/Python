#For Loop Practice:

#Problem 1: Sum of Natrual Numbers
"""
num = 0
count= 0
for num in range(1, 101):
    num += num
    count += 1
    print(num)
    print(count)
"""

#Problem 2: Print Multiplication Table
"""
for num in range(1, 11):
    num = num * 7
    print(num)
"""

#Problem 3: Reverse a String
"""
char = ""
phrase = str(input("Enter a phrase: "))
for index in range(len(phrase)-1, -1, -1): #reverse the str
    char += phrase[index]
print(char)
"""

#Problem 4: Count Even and Odd Numbers:
"""
even = 0
odd = 0
for num in range(1, 10):
    if num % 2 == 0:
        even += 1
    elif num % 2 == 1:
        odd += 1
print(f"There is {even},even numbers.")
print(f"There is {odd},odd numbers.")
"""

#Problem 5: Print All Prime Numbers
