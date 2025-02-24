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

"""n = int(input("Enter a number: "))
for i in range(-n, n):
    if i < 0:
        negative: True
    if i > 0:
        positive: True
    print("The number is positive:", positive)
    print("The number is negative:", negative)
"""
"""Nested loops"""

"""for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print("Time:", str(hour)+":"+str(minute)+":"+str(second))"""

""""Practice Problem:"""

"""Write a program that prints a multiplication table for number 1 through 5. 
The output should look like this"""

"""for row in range(1,6):
    for col in range(1,6):
        print(row*col, end ="\t")
    print() """ """Once they print the multiple of 1 the print() breaks it so it prints the 
    multiple of 2 on the next line, etc."""

"""8) create a program that prints a table of squares from 1 to n"""
"""
number = int(input("Enter a number: "))
for num in range(1, number+1):
    print(num, num **2)
"""

"""stars = int(input("How many stars do you want?"))
row = 1
while row <= stars:
    for col in range(1, row+1):
        print("*", end="")
    row += 1
    print()

stars = int(input("How many stars do you want?"))
for row in range(1, stars+1):
    for col in range(1, row+1):
        print("*", end="")
    print()"""

"""Body Mass index calculator"""
"""BMI = weight (kg)/ height (n)** 2"""

"""weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (n): "))

body_mass_index = weight / (height ** 2)

print("BMI:", round(body_mass_index,2))"""

"""Body Mass index calculator"""
"""BMI = weight (kg)/ height (in)** 2"""

"""weight = float(input("Enter your weight (lbs): "))
height = float(input("Enter your height (in): "))
for height in range(54, 83, 2):
    for weight in range(85,350, 5):
        body_mass_index = height/weight ** 2 * 703
        print(weight, height, "BMI:", round(body_mass_index,2))"""

"""2)Write a program that prints aright-angled triangle of numbers.For an input n, 
the out put should look like this:"""

"""n = int(input("Enter a number: "))

for row in range(1, n+1):
    for col in range(1,row+1):
        print(row, end="")
    print()
"""
"""3) Create a program that prints a pyrimid of stars (*).
For an input n, the output should look like this."""

"""star = int(input("Enter a number: "))

for row in range(star):
    for col in range(star-row-1):
        print(" ", end="")
    for column in range(2 * row + 1):
        print("*", end="")
    print()"""

"""4)Write a program that prints an inverted triangle of numbers.
For an input n, the out put should look like this """

"""n = int(input("Enter a number: "))

for row in range(n, 0, -1):
    for col in range(row, 0, -1):
        print(row, end="")
    print()"""

"""5)Write a program that prints Floyd's triangle.
The first n rows of the triangle should be filled with consecutive numbers.
For an input n, the out put should look like this: """

"""n = int(input("Enter a number: "))
num = 1

for row in range(1, n+1):
    for col in range(row):
        print(num, end=" ")
        num += 1
    print()"""

"""6)Create a program that prints a diamond shape made of stars.
For an input n, the output should look like this:"""

#star = int(input("Enter a number: "))

"""for row in range(0, star):
    for col in range(star-row-1):
        print(" ", end="")
    for column in range(2 * row + 1):
        print("*", end="")
    print()
for row in range(0, star - 1):
    for col in range(0, row + 1):
        print(" ", end="")
    for column in range((star-row-1)*2-1):
    #for column in range((star- 1)*2 - (row)*2-1): # 7, 6, 5 ,4
        # 7 5 3 1
        print("*", end="")
    print()"""


"""7)Writea program that prints a chess board pattern using a sterisks(*)and spaces.
For an input n, the output should look like this:"""

"""star = int(input("Enter a number: "))
extra = False

for row in range(star):
    if extra == True:
        print(" ", end="")
    for i in range(star):
        print("*", end=" ")
    extra = not extra
    print()
    
star = int(input("Enter a number: "))

for row in range(star):
    if row % 2 == 1:
        print(" ", end="")
    for i in range(star):
        print("*", end=" ")
    print()"""


n = int(input("Enter a number: "))

for row in range(1, n+1):
    for col in range(1, row+1):
        print(row*col, end=" ")
    print()

"""n = int(input("Enter a number: "))

for i in range(0, n+2):
    print("*", end="")
print()

for row in range(0, n-2):
    #print("*" + " "*n +"*")
    print("*", end="")
    for col in range(0, n):
        print(" ", end="")
    print("*")

for i in range(0, n+2):
    print("*", end="")
print()"""