#String

# my_str = ("hello_world")
#
# print(my_str[7])
#
# course_name = "CS1114"
#
# print(course_name[0])
#
# result = "C"

#Gives me the 7th sequence in the string, in this case it would be "o"

#Comparison (relational) operators

# "Apple" == "apple"
#
# result = false

#and : return the unicode value for char

"""print(ord('}'))"""

# char: returns the char given a Unicode

"""print(chr(115000))"""

# A-Z before a-z

#The in operator

# sub_str in string => True/False
#
# "sam" in "sampling" => true

# "net" not in "onetwothree"
#
# false because "net" is in it

# \n = break  \t = tab

"""print(ord('\n'))"""

#str objects

# my_str = "food"
"""print(my_str.capitalize())
print(my_str)
"""
"""print(my_str.replace("od","dinner"))"""

"""print(my_str.find("d"))"""
#locates a substr and return its start index, 3 in the case with food and d
#if we try to find something not avalible it will return -1

# string slicing

# my_str[start:stop]
#
# my_str[0,5] => "hello" 0-4 not including 5


#f - string
"""salary = 5000000.5

output = f"{salary:.3f}"
print(output)"""

"""num1=10
num2=145
num3=6789

print(f"{num1:> 6}")
print("{:>10}".format(num2))
print(f"{num3:^6}")"""

"""num1 = ("programming")
num2 = ("is awesome!")
joined = 0

joined = str(num1) +" "+ str(num2)

print(joined)"""

"""word = 'playground'
two_letters = 0
two_letters = word[4] + word[-3]
print(two_letters)"""

"""my_string = 'supercalifragilisticexpialidocious'
print(my_string[-10:])"""

"""sentence = 'I like it!.'

it_count = sentence.count('it')

print(it_count)"""

"""sentence = 'That idea is awesome!'

print(sentence.replace('idea', 'though'))"""

"""num1 = 'happybirthday'
num2 = 'happybir98987'
"""
"""if num1.count(len(num1)) > num2.count(num2):
    print(num1)
elif num1.count(num1) < num2.count(num2):
    print(num2)
elif num1.count(num1) == num2.count(num2):
    print(num1)
    """
"""if len(num1)>=len(num2):
    print(num1)
else:
    print(num2)"""

"""phrase = 'Python'

if len(phrase) < 7:
    print("short")
elif len(phrase) > 20:
    print("long")
else:
    print("medium")
"""
