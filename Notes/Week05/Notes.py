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

num1=10
num2=145
num3=6789

print(f"{num1:> 6}")
print("{:>10}".format(num2))
print(f"{num3:^6}")