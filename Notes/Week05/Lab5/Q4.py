#4



"""text = input("Input the mad lib text: ")
adjective = input("What's your adjective? ")
verb = input("What's your verb? ")
noun = input("What's your noun? ")
number = input("What's your number? ")
print("Creating mad lib...")

text = text.replace("V", verb)
text = text.replace("A", adjective)
text = text.replace("N", noun)
text = text.replace("U", number)

print(text)"""
madlib = input("Input the mad lib text: ")
madlib_char = "AVNU"
final_str = ""
for i in range (len(madlib)):
    if madlib[i] in madlib_char:
        if madlib[i] == "A":
            adjective = str(input("What's your adjective? "))
            final_str += adjective
            #print()
        elif madlib[i] == "N":
            noun = str(input("What's your noun? "))
            final_str += noun
            #print()
        elif madlib[i] == "V":
            verb = str(input("What's your verb? "))
            final_str += verb
            #print()
        elif madlib[i] == "U":
            number = str(input("What's your number? "))
            final_str += number
            #print()
    else:
        final_str += madlib[i]

print("Creating mad lib...")
print(final_str)


