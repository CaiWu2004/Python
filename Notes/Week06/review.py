#1)Programming Aliens Language

"""def main():

    #get the user input
    human_word = input("Enter a human word: ")

    #double every vowel
    doubled_word = ""
    for char in human_word:
        if char in "AEIOUaeiou":
            doubled_word += char * 2 # double the char
        else:
            doubled_word += char #keep the char as is

    # reverse word
    reversed = doubled_word[::-1]

    # add prefix and uppercase
    alien_word = f"ZYX-{reversed}".upper()
    alien_word = "ZYX-"+reversed.upper()

    #print the output
    print("\nTranslated word:")
    print(f"\t{alien_word}")

main()"""

#2)

cake = str(input("Cake flavor: "))
ingredient1 = str(input("First Ingredient: "))
ingredient2 = str(input("Second Ingredient: "))
ingredient3 = str(input("Third Ingredient: "))


combo1 = cake[0:3] + ingredient1[-3:]
combo2 = cake[0:3] + ingredient2[-3:]
combo3 = cake[0:3] + ingredient3[-3:]
combo1 = combo1.upper()


print(combo1)
print(combo2)








