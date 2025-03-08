sheets = int(input("Enter the number of sheets of paper you use per day: "))
while sheets <= 0:
    sheets = int(input("Invalid input. Enter a non zero numerical value: "))
number_of_trees_per_day = sheets/ 8000
number_of_trees_per_year = number_of_trees_per_day * 365

print("\nEnvironmental Impact Analysis:")
print(f"-Number of trees needed: {number_of_trees_per_day:.2f}")
print(f"-Annual consumption of trees:{number_of_trees_per_year:.2f}")

if number_of_trees_per_year < 5:
    print("-Your paper usage is considered sustainable.")
elif number_of_trees_per_year <= 10:
    print("-Your paper usage is considered moderate.")
else:
    print("-Your paper usage is considered unsustainable.")

