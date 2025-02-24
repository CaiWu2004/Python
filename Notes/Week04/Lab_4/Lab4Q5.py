
space = int(input("Python needs to tell you a secret. How many characters wide can its message be?: "))


for row in range(1, space +2):
    for column in range(1, row):
        if column in range(1, row):
            print("X",end="   ")
            print("X")
        if column in range(1, row+1):
            print(end=" ")
            print("X","X")
        if column in range(1, row+2):
            print(end="  ")
            print("X")
        if column in range(1, row+3):
            print(end=" ")
            print("X","X")
        if column in range(1, row+4):
            print("X", end="   ")
            print("X")
        print()

for row in range(1, space + 2):
    for column in range(1, row +5):
        if column % 2 == 0:
            print("","O"*3,"")
        if column % 2 != 0:
            print("O"," ","O")
        print()

