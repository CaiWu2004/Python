#6

phrase = input("Please enter your message: ")


phrase += " "

start_ind = 0
secret_phrase = ""

for i in range(len(phrase)):
    char = phrase[i]

    if char == " ":
        word = phrase[start_ind:i]

        if word[0].isupper() and word[1].islower():
            secret_phrase += word[0]

        start_ind = i + 1
print("Your secret message is:", secret_phrase)




"""    print(phrase[i], end="")"""

