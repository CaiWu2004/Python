"""age = input("Enter age? ")

while not age.isdigit():
    age = input("Invalid input. Enter age? ")

print(f"{age} is valid")
"""
"""from ast import Num"""

"""message = "Hello World!"

print(message[5].isspace())"""


"""message = "CS1114 is a cool class."""

"""print(message.split())"""

"""print(message.strip())"""

"""print(message)"""

""""
new = message.strip()

print(new[:5])
print(new[:5:2])

var = message.find("X")
print(new[:-6:var]) # .ssal
print(new[::-1])

number = 7
print(f"{number:>04}") #0007
"""

#function

"""
def function_name():
    statement
    statement"""


#6)Converting =

#practice problem 12)

"""def decimal_to_binaru(n):
    if n == 0:
        return "0"
    if n < 0:
        n = -n # work with positiive for convers
    binary_str = ""
    while n > 0:
        binary_str = str(n%2) + binary_str # repand the reainder n//2
        n //=2

    return binary_str

def main():
    print(decimal_to_binaru(0))

main()"""

#5)

#def count_vowels(s):
""" 
    counts and returns the number of vowels in a given string
    :param s (str)
    :returns int
    """
"""    s = s.upper()
    num_vowels = 0
    for char in s:
        if char in "AEIOU":
            num_vowels +=1
    return num_vowels


def main():
    print(count_vowels("Harry"))

main()"""

"""def count_vowels(s="Alex"):

    s = s.upper()
    num_vowels = 0
    for char in s:
        if char in "AEIOU":
            num_vowels+=1
    return num_vowels

def main():
    print(count_vowels("Harry"))

main()"""


