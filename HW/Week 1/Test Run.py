
#height = int(input("Height"))
#feet = height // 12
#inches = height % 12
#print("That person is",feet,"feet and",inches,"inches tall.")
'''''
import math
degree = float(input("Please enter an angle in degrees (float):" ))
tangent = math.tan(math.radians(degree))
print(tangent)
'''

"""num_people = 9

print(str(num_people) +" people" if num_people != 1 else "1 person")"""
""""import math
value = 0

while value < 30:
    value += 1
    if value < 30:
        print(math.sqrt(value))
    else:
        print("value is greater than 30")
"""
"""min_val = 1
max_val = 6
print("Kilograms\tPounds")

kg = min_val

while kg <= max_val:
    pounds = kg * 2.2
    print(f"{kg}\t{pounds:.2f}")
    kg += 1
"""
"""start_val = 1
stop_val = 5
counter = 0
while start_val <= stop_val:
    counter += 1
    start_val += 1

print(f"The loop executed {counter} times.")"""

"""min_val = 1
max_val = 6
print("Kilograms\tPounds")

kg = min_val

while kg <= max_val:
    pounds = kg * 2.2
    print(kg, "\t", pounds)
    kg += 1"""

"""word = "box"

for letter in word:
    print(letter, letter)"""
"""
for val in range(5, 10):
    print('wow')"""
""""
list = [2, 4, 6, 8, 10]

num = 0
for val in list:
    if val != 6:
        num = num + val
print(num)"""

"""for num in range(250, 300):
    sum = num + num
    print('The sum of',num,'is',sum)"""

import math
print(math.sqrt(4))