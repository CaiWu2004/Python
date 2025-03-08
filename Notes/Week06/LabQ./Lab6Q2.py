#2) Roman Code(r):

def decode_part(msg, start, end, step):
    return msg[start: end: step]


def decode_entire_msg(msg):
    msg += "1"
    letter_count = 0
    step = int(msg[0])
    start = 1
    ind = 1
    output_msg = ""

    while letter_count < 100 and ind < len(msg):
        if msg[ind].isdigit():
            end = ind
            output_msg += decode_part(msg, start, end, step)

            step = int(msg[ind])
            start = ind + 1

        if msg[ind].isalpha():
            letter_count += 1
        ind += 1

    return output_msg

def main():
    """
    Test your code here
    """
    message = "3Gn.olwo pd/Q gh5l!d pulAk c_kosk an2 moPn! .y\oausr? 3mqei,sd+ktcbe.KrkcmOpsne!se odYpqo>kulq fag pozrtks dftpqh /ipaslk!dp4vm fkofwolp9 mjcnre"
    print(decode_entire_msg(message))

main()



"""fuel = 100 # Initial rocket fuel
launches = 1 # Number of rocket launches
while fuel > 0:
    print(launches,"launches:", end = "")
    for consumption in range(fuel, 0, -fuel//5):
        print(consumption, "->", end = "")
    if fuel > 10:
        print("Blastoff!")
    else:
        print("Rocket grounded.")

    fuel //= 5 # Sim
    launches += 1"""


def func1(var):
    return var + 1
def func2():
    return 57 + func1(42)
def func3(var):
    if func2() >= var:
        return func1() + func2()
    else:
        return 0
def func4(var):
    print(var + func3(50))

def main():

    n = 10
    n = func2()

main()





