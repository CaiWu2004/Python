#2) Higher and Higher

number_of_values = int(input("Please enter how many positive values you want to consider: "))
greatest = 0
print("Enter your values: ")

for _ in range(1, number_of_values+1):
    val = float(input())
    if val > greatest:
        greatest = val
print("The largest of these values is", greatest)