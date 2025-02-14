print("This is a four operation calculator.")

enter = input("Press enter to continue and Q to quite calculator.")
num1 = float(input("Enter first number: "))
operation = input("Enter your operation(+, -, *, /): ")
num2 = float(input("Enter second number: "))
print(num1, operation, num2, "=", eval(str(num1) + operation + str(num2)))

while enter != "Q":
    enter = input("Press enter to continue and Q to quite calculator.")
    if enter == "":
        num1 = float(input("Enter first number: "))
        operation = input("Enter your operation(+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        print(num1 ,operation,num2, "=" ,eval(str(num1)+operation+str(num2)))
else:
    print("Goodbye!")
