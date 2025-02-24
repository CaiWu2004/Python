#For and Nested Loop Glare

#1.a)
"""for num in range(0,10):
    print(num)"""
from libpasteurize.fixes.fix_imports2 import from_import

"Will print numbers from 0-9 inclusive straight down"

#1.b)

"It will print numbers from even integers starting at 1 to 12 inclusive"

#1.c)

# It will print numbers from 43 to 30 inclusive down by
#  value of 3 which means it will
#  start at 43, 40, 37, 34

#1.d)

"""for num in range(4):
    for val in range(4):
        print(num*val, end=" ")
    print()"""

#It will print a multiplication grid where there will be 4 rows
#then it will print 4 columns since the range if 4.
#These tow and columns will print from 0 to 3 and its products down

#1.e)

"""for num in range(5):
    for val in range(num+1, 5):
        print(num, val)"""

#This will print out the values of num in relations of val.
#the value of num will start out with 0 and then next to it will print
#the value of val which is starts at num+1. This meant that when num start
#at 0, val will be 1 and printed next to it. The result is also that
#they will print out the numbers for val from start to end next to the first
#value of num which is 0.
# Then it will print num as the next number which is 1. When num is 1, the
# starting value of val is num + 1 which this case is 2. And like the first
# value in num, they will print out all the value of val in relations to the second
# value of num until 4. This goes on until the value of val reaches 4 even if the value
# of num doesn't because val is num + 1.

#1.f)

"""for num in range(1,10):
    if num % 2 == 0:
        for val in range(num, 10, 2):
            print(val, end = " ")
        print()"""

# This nested for loop will print a reverse triangle where the top
# is the base downwards. This is printing even numbers from 1-9 inclusive.
# This function will print out the rows and columns depending on
# how many even numbers are in the range values. In this case from 1-9 which is
# 4 and them being 2,4,6,8. The first column will start from all even numbers from
# 1-9. Then it will break into the next column which starts at the next even number that comes
# after the first number in the first column. That means it prints out
# 2,4,6,8 in the first column, break then print out 4,6,8 in the next column
# because for the first row it also prints the even numbers for 1-9 facing down.
#As they print the last even number in each column will also create a space depending on the
#column it is in.

#1.g)

"""for i in range(1,10):
    if i%2 ==0:
        for j in range(0, i, 2):
            print(j, end=" ")
        print()"""

#it prints a even values from 0-8 starting at 0,
#in this case 4 rows because it is printing out
#4 different values, 0,2,4,6
#First column is 0, then 2, 4, 6
#depending on the column the number of space is also different
#After printing out the values in each column it
#will fill the rest of the row with empty spaces then break


even_sum = 0

for num in range(2, 100):
    if num % 2 == 0:
        for val in range(2, num):
            even_sum += num

        print(even_sum)
