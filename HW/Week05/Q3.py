"""
Author: [Harry Wu]
Assignment / Part: HW5 - Q3
Date due: Mar 6, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""
#input the string=all lowercase
letters = str(input("Enter a string of lowercase letters: "))
#if the user had enter nothing = empty string and were going to
# determine its a decreasing string so its true at default
result = True
#what index was it decreasing at: default is -1, beginning form beginning to end
result_index = -1
#skip the first letter because its either no letter or only 1 letter:
for index in range(1, len(letters)):
    char = letters[index]
    prev_char = letters[index - 1]
    #this is comparing the second char to the first and result tell us if we have already seen an increase
    #if abgcp we saw an increase at ab which is the first increase, we then track it so we make sure
    #we only lock in the first time its increasing and not the last time
    if result and char > prev_char:
        result = False
        result_index = index

if result:
    print(f"{letters} is decreasing")
else:
    print(f"{letters} is not decreasing."
          f"\nIt stopped being lexicographically decreasing at location {result_index}")



