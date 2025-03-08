"""
Author: [Harry Wu]
Assignment / Part: HW5 - Q4
Date due: Mar 6, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

encoded_string = input("Enter an encoded string: ") #takes the code/what I type
key = int(input('Enter a key: '))


"""encoded_string = encoded_string[-1::-1]
print(encoded_string)"""
#looking at the index of the input and reversing it. And I am skipping
#every charather based on the steps/key i enter
for index in range(len(encoded_string)-1, -1, -(key+1)):
    char = encoded_string[index]
    #print(char, end="")
#if the char is not a number it will print it based on the
#rule that we are skipping every key char
    if not char.isdigit():
        print(char, end="")











# take the indexes from the beginning of the length of my
# inputed code/words
# and then listed it out in order like 0,1,2,3,4
# downwards
#for words in range(1, len(encoded_string)):
# this parts read the indexes and make sure I get the letter/strings instead of the index
# the end="" part make sure they are listed from left to right
    #print(encoded_string[words], end="")
