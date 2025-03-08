"""def is_armstrong(num):
    if (num // 100) ** 3 + ((num // 10) % 10) ** 3 + (num % 10) ** 3 == num:
        return True
    else:
        return False"""

"""x =10

def abc():
    return("hello")

def xyz(x):
    print(x)
    return x ** 2

def qwe(y):
    print(xyz(y))

def main():

    print(abc()) #hello
               #None
   # print("_________________")
    print(xyz(2)) #2
                  #4
    #print("__________________")
    print(qwe(4)) #4
                  #16
                #None"""

"""def is_leap_year(year):
    le_year = int(year)
    if le_year % 4 == 0 or le_year & 400 == 0:
        if le_year >= 1582:
            return True
        else:
            return False
    else:
        return False

print(is_leap_year(1900))"""

"""def is_leap_year(year):
   if year > 1582:
       if year % 4 == 0:
           if year % 100 == 0:
               if year % 400 == 0:
                   return True
               return False
           return True
       else:
           return False
   else:
        return False"""


"""def compute_pay(hourly_wages, num_hours):
    take_home = 0
    taxes = 0
    medical = 0

    if num_hours <= 40:
        total_wage = num_hours * hourly_wages
    else:
        total_wage = (40 * hourly_wages) + ((num_hours - 40) * hourly_wages * 1.5)

    taxes = total_wage * (20 / 100)
    medical = total_wage * (10 / 100)
    total = taxes + medical
    total_wage = total_wage - total

    return round(total_wage, 2)

print(compute_pay(12.25, 45))"""

"""def ordinal_sum(argument):
    sum = 0
    for index in range(0, len(argument)):
        word = argument[index]
        print(word, end="")"""

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
    n = func3(200)
    print(func4(func3(100)))

main()




