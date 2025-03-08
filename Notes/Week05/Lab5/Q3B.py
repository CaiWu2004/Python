#3B

phrase = input("Enter a phrase: ")

for index in range(len(phrase)-1, -1, -1):
    print(phrase[index], end="")
    #reverse_phrase = phrase[len(phrase)-1-index]