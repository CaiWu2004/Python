#5

text = input("Enter a phrase: ")

text += " "
hidden_string = ""
start_ind = 0

for index in range(len(text)):
    char = text[index]

    if char == " ":
        word =  text[start_ind:index]

        if word.isdigit():
            hidden_string += ("X" * len(word))
        else:
            hidden_string += word

        hidden_string += " "

        start_ind = index + 1

print(hidden_string)









"""print(phrase[index], end="")"""
"""
if phrase[index].isalpha() != True and phrase[index].isalnum() != True:
        phrase[index].replace(phrase[index], "X")"""
"""    
    if phrase[index] == index.isdigit():
        phrase.replace()"""

"""if phrase.isdigit():
    phrase.replace(" ", "X")
print(phrase)"""