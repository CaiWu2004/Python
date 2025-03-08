#String Comparisons:
"""
Write a program that asks the user to input an original
string and continuously enter more strings.
The program should track how many of the new strings are both
lexicographically greater than the original string and the
previous string entered.
"""
"""
Enter original string: Alpha
Enter a string (-1 to quit): Beta
Enter a string (-1 to quit): Charlie
Enter a string (-1 to quit): Apple
Enter a string (-1 to quit): -1
Percentage: 50.0%
"""

#Environmental Impact Calculation:
"""
Write a program that calculates the environmental impact of plastic bottle usage.

1.Prompt the user for the number of plastic bottles used daily.
2.Assume that one plastic bottle takes 450 years to decompose.
3.Calculate and display:
    -The estimated annual number of plastic bottles used.
    -The total years it would take for them to decompose.
"""

"""
Example:
Enter daily plastic bottle usage: -3
Invalid input. Enter a positive numerical value: 5

Environmental Impact:
- Annual usage: 1825 bottles
- Decomposition time: 821250 years
"""

"""
bottle_per_day = int(input("Enter the number of plastic bottles used daily: "))

while bottle_per_day < 0:
    bottle_per_day = int(input("Invalid input. Enter a positive numerical value: "))
annual_bottle_usage = bottle_per_day * 365
decomposition_time = annual_bottle_usage * 450

print("\nEnvironmental Impact:")
print(f"-Annual usage: {annual_bottle_usage} bottles")
print(f"-Decomposition time: {decomposition_time} years")
"""

#1) Boolean Expression & Order of Operations
#Evaluate the following expressions using the given values
"""
a = 8  
b = 3  
c = 5  
d = 10  
e = 2  
f = 7  
g = 4  
h = False  
i = True  

# Evaluate the following expressions:
1. a ** e + c * 3 = 8 ** 2 + 5 * 3 = 64 + 5 * 3 = 64 + 15 = 79
2. f + d % b * a - e  = 7 + 10 % 3 * 8 - 2 = 7 + 10 % 24 -2 = 7 + 0 - 2 = 7 -2 = 5
3. d // (b + e) * c  = 10 // (3 + 2) * 5 = 10 // (5) * 5 = 10 // 25 = 0
4. (e * (f - c) >= 12) or i  = (2*(7 - 5) > = 12) or true = (2*(2) >= 12) or true= 4 >= 12 or true = false or true= true
5. c * a == b + f or h and i = 5 * 8 == 3 + 7 or false and true = 40 = 21 or false and true = false or false and true = false and true = false
6. c == g // (a + e - f) and not h = 5 == 4 // (8 + 2 - 7) and not false = 5 == 4 // (3) and not false = 5 == 1 and not false = false and not false = false
"""

#Loops & Conditionals:
"""
water = 50  # Initial water supply
refills = 1  # Number of refills

while water > 0:
    print(refills, "refills:", end=" ")
    for usage in range(water, 0, -water // 4):
        print(usage, "->", end=" ")
    if water > 8:
        print("Still going!")
    else:
        print("Water depleted.")

    water //= 4  # Water consumption per cycle
    refills += 1
"""
"""
output:
1 refills: 50 -> 38 -> 26 -> 14-> Still going!
2 refills: 12 - 9 -> Still going!
3 refills: 2 -> Water depleted!
needs to be explain
1 refills: 50 -> 37 -> 24 -> 11 -> Still going!
2 refills: 12 -> 9 -> 6 -> 3 -> Still going!
3 refills: 3 -> 2 -> 1 -> Water depleted.
"""



#Functions & Errors:
"""
def fun1(x):
    return x + 2

def fun2():
    return 20 + fun1(10)

def fun3(x):
    if fun2() <= x:
        return fun1() + fun2()
    else:
        return -1

def fun4(x):
    print(x + fun3(30))

def main():
    y = 5
    # Insert a function call here

# Determine if these function calls are valid or errors:
1. fun1(y)
2. y = fun2()
3. print(fun4(fun3(50)))
4. fun4(y)
5. y = fun3(100)
"""

#Environmental Impact Calculation:
"""
Write a program that calculates the environmental impact of plastic straw usage.

1.Prompt the user for the number of plastic straws used daily.
2.Assume that one plastic straw takes 200 years to decompose.
3.Calculate and display:
    -The estimated annual number of plastic straws used.
    -The total years it would take for them to decompose.
    
example:
Enter daily plastic straw usage: -2  
Invalid input. Enter a positive numerical value: 8  

Environmental Impact:  
- Annual usage: 2920 straws  
- Decomposition time: 584000 years 
"""
"""
daily_straws = int(input("Enter daily plastic straws usage: "))

while daily_straws < 0:
    daily_straws = int(input("Invalid input. Enter a positive numerical value: "))

annual_straws = daily_straws * 365
decomposition_time = annual_straws * 200

print("\nEnvironmental Impact:")
print(f"-Annual usage: {annual_straws} straws.")
print(f"-Decomposition time: {decomposition_time} years.")
"""

#String Comparisons:
"""
Write a program that asks the user to input an original string and continuously 
enter more strings. The program should track how many of the new strings are 
both lexicographically greater than the original string and the 
previous string entered.

Example input/output:
Enter original string: Cat
Enter a string (-1 to quit): Dog
Enter a string (-1 to quit): Elephant
Enter a string (-1 to quit): Ant
Enter a string (-1 to quit): -1
Percentage: 50.0%
"""