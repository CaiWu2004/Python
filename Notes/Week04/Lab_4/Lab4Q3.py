#3) Line by Line

string = input("Enter a string to be printed ( in the format [text]-[text] ...)")

for char in string:
    if char == "-":
        print()
    else:
        print(char, end="")
