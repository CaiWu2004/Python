"""Condition Control Loop(while loop)/Count Control Loop(for loop"""

"""my_seq =list(range(1,10)) #1,2,3,4,5,6,7,8,9
my_seq =list(range(10))
my_seq2 = list(range(1,10,2))
print(my_seq)
print(my_seq2)"""

"""for sum in range(250, 300):
    print(sum+sum, end=",")"""

"""for iter in range(1,250):
    iter += 1
    print(iter, end=" / ")"""

"""for char in 'python': #P, y, t,h,o,n
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(number, ": Even")
    else:
        print(number, ": Odd")"""

"""sum = 0
for num in range(1,101):
    sum += num
    print("The sum is", sum)"""
"""from math import sqrt, ceil
number = int(input("Enter an integer value: "))
prime = True
for it in range(2, number):
for it in range(2, ceil(sqrt(number))):
    if number % it ==0:
        prime = False
print(number, "is prime:", prime)

"""

n = int(input("Enter a number: "))
for i in range(-n, n):
    if i < 0:
        negative: True
    if i > 0:
        positive: True
    print("The number is positive:", positive)
    print("The number is negative:", negative)
