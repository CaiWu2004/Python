"""1a:"""
"""The final value is 0 because 
its incrementing y by 1 since 15 % 2 is 1 
it leads to false if y % 2== 0"""

"""1b"""

"""num = 1
while num < 28:
    print( num)
    num *= 3"""
"""This while loop prints out multiples of 3 starting at 1 and end at 27 
because if its increment by a multiple of 3 
again it will be greater than 28"""

"""1c"""

"""num = 13
while num < 23:
    if num % 2 ==0:
        print(num)
    else:
        print("fizz")
    num += 1 """

"""Its going to print out fizz 
 every odd number starting with 13 and then even 
 numbers starting at 14 until it reaches 22 """

"""1d"""

"""Going to keep incrementing num by 1 until it's less then 50 by is 
diviable by 5 and 10 an the remainder is 0 then it will print fizz and buzz until
num has been incremented above a value of 50 which will then print put 
FIZZ and BUZZ until num is 99"""

num = 1
while num < 100:
    if num > 50:
        if num % 10 == 0:
            print("FIZZ")
        elif num % 5 == 0:
            print("BUZZ")
    else:
        if num % 10 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
    num += 1

"""Prints a total of 19 times where from 1-10 is alternating between 
buzz and fizz starting from buzz and then it 
starts print FIZZ and BUZZ from 11 -19 starting at BUZZ"""