from setuptools.windows_support import hide_file

decimal_num = int(input("Enter a decimal number less than 100: "))

string = ((decimal_num // 50) * "L")
string += (decimal_num % 50) // 10 * "X"
string += (decimal_num % 10) // 5 * "V"
string += (decimal_num % 5) * "I"

print(string)






