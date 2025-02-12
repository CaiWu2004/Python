num1 = float(input("Enter your first number: "))
operation = input("Enter your operation(+, -, *, /): ")
num2 = float(input("Enter your second number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print( num1,"/", num2, "is an invalid operation.")
    else:
        print(num1 / num2)