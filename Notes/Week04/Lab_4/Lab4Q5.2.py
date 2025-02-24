
space = int(input("Python needs to tell you a secret. How many characters wide can its message be?: "))


for row in range(0, space):
    for column in range(space):
        if column == row:
            print("X",end="")
        elif column + row == space - 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()

for row in range(space):
    for column in range(space):
        if row == 0 or row == space-1:
            if column == 0 or column == space-1:
                print(" ", end="")
            else:
                print("O", end="")
        else:
            if column == 0 or column == space-1:
                print("O", end="")
            else:
                print(" ", end="")
    print()

for row in range(0, space):
    for column in range(space):
        if column == row:
            print("X",end="")
        elif column + row == space - 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()


print("- From Python")