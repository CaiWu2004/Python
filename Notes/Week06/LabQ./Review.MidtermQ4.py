"""
origin = ""
new = ""
original = input("Enter the original string: ")
origin += original
sentence = input("Write something (-1 to quite): ")
new += sentence
percentage = 100
while sentence != "-1":
    sentence = input("Write something (-1 to quite): ")
    if sentence != "-1":
        new += sentence
    else:
else:
    print(f"Average:{percentage}%")
"""
count_true = 0
count_all = 0

#The og string,
original = input("Enter the original string: ")
previous_string = ""
#Repeately as for a new string
current = input("Write something (-1 to quite): ")

while current != "-1":
    if current > previous_string and current > original:
        count_true += 1
    count_all += 1
    previous_string = current
    current = input("Write something (-1 to quite): ")
print(f"average:{(count_true/count_all)*100}%")

