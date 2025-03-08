#1) Function Fun
"""
def mystery(num, string):
    secret = ""
    for char in string:
        secret += char * num
    return secret

def main():

    print(mystery(5, "hello"))

main()"""

#Print hello 5 times where each characther is side by side. For example "HHHHHeeeeellllllllllooooo"

def func_one(val):
    num = 10
    if val % 3 == 0:
        print(num)
        print("whoop")
        return True

def func_two(num):
    while num < 20:
        if func_one(num):
            print(num)
        num += 1
    print(num)

def main():
    func_two(13)
main()

# 13 is inputed into func_two(num), its less then 20 so it goes to func_one(val) where val is replace with num=13.
# it passess num = 10, and it does not pass through the if loop because 13 % 3 is not == 0. It goes back to num_two
#whrere it goes to num += 1 because it did not pass the condition of if func_one(num):
# it then prints 14 and it goes to num and this loop goes on until it reach 19.
#if a number does pass through the condition val % 3 == 0: it will print out 10, "whoop" becuase num is always = 10 in num_one loop