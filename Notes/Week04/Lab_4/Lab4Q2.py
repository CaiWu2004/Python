#2) Higher and Higher

number_of_values = int(input("Please enter how many positive values you want to consider: "))
values = 0
print("Enter your values: ")

for val in range(1, number_of_values+1):
    val = float(input())
    if val > values:
        values = val
print("The largest of these values is", values)