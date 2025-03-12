#Conditional Expression Problems:

"""
Create a program that asks the user to input a temperature. Based on the input,
set the variable status to "hot"
if the temperature is greater than 30, otherwise set it to
"cold".
"""

"""temperature = int(input("Enter a temperature: "))

if temperature > 30:
    print("Hot")
else:
    print("Cold")"""

"""
Write a program that prompts the user to enter a number. 
Set the variable sign to "positive" if the number is greater than 0, 
otherwise set it to "negative".
"""

"""num = int(input("Enter a number: "))
sign = ""
if num > 0:
    sign = "positive"
    print(sign)
else:
    sign = "negative"
    print(sign)"""

'''
Create a program that takes the user’s input for their current speed. 
Set the variable speed_category to "fast" if the speed is greater than 60, 
otherwise set it to "slow".
'''

"""current_spd = int(input("Enter a current speed: "))
speed_category = ""
if current_spd > 60:
    speed_category = "fast"
    print(speed_category)
else:
    speed_category = "slow"
    print(speed_category)"""

"""
Write a program that asks the user for their age. 
Set the variable discount to 10 if the age is greater than 65, 
otherwise set it to 0.
"""

"""age = int(input("Enter your age: "))
discount = 0
if age > 65:
    discount = 10
    print(discount)
else:
    discount = 0
    print(discount)"""

"""
Create a program that asks the user to input the current day of the week. 
Assign the variable day_type to "weekend" if the day is "Saturday" or "Sunday", 
otherwise set it to "weekday".
"""

"""
day_of_week = str(input("Enter the current day of the week: "))
day_type = ""
if day_of_week == "Saturday" or day_of_week == "Sunday":
    day_type = "weekend"
    print(day_type)
else:
    day_type = "weekday"
    print(day_type)
"""

# If-Else Statement Problems:

"""
Create a program that prompts the user to input a number. 
If the number is greater than 0, set result to "positive", 
otherwise set it to "negative".
"""

"""
num = int(input("Enter a number: "))

if num > 0:
    result = "positive"
    print(result)
elif num < 0:
    result = "negative"
    print(result)
"""

"""
Write a program that asks the user to input the current weather 
(either "sunny" or "rainy"). If the weather is "sunny", 
set the variable mood to "happy", 
otherwise set it to "gloomy".
"""

"""
weather = str(input("Enter a weather(sunny or rainy): "))

if weather == "sunny":
    mood = "happy"
    print(mood)
elif weather == "rainy":
    mood = "gloomy
"""

"""
Create a program that asks the user for their age. 
If the user is older than 60, set discount to 20, 
otherwise set it to 0.
"""

"""age = int(input("Enter your age: "))

if age > 60:
    discount = 20
    print(f"You are older than 60 and has a discount of {discount}%")
elif age < 60:
    discount = 0
    print(f"You are not yet 60 and has a discount of {discount}%")"""

"""
Write a program that takes the user's test score as input. 
If the score is 50 or higher, set result to "pass", 
otherwise set it to "fail".
"""

"""
score = int(input("Enter your test score: "))
if score > 50:
    result = "pass"
    print(f"You {result}!")
elif score < 50:
    result = "fail"
    print(f"You {result}!")
"""

"""
Create a program that asks the user to 
input the color of a traffic light ("red" or "green"). 
If the light is "red", set the action to "stop", 
otherwise set it to "go".
"""

"""traffic_light = str(input("Enter your traffic light color: "))

if traffic_light == "red":
    action = "stop"
    print(f"You need to {action}!")
elif traffic_light == "green":
    action = "go"
    print(f"You can {action}!")"""

# If-Else if-Else Statement Problems:

"""
Write a program that asks the user for the current temperature. 
If the temperature is greater than 30, assign the variable category to "hot". 
If it's between 15 and 30, assign it to "warm". Otherwise, assign it to "cold".
"""

"""temperature = int(input("Enter current temperature: "))

if temperature > 30:
    category = "hot"
    print(category)
elif temperature > 15 and temperature < 30:
    category = "warm"
    print(category)
elif temperature < 15:
    category = "cold"
    print(category)"""

"""
Create a program that prompts the user to enter a test score. 
If the score is 90 or above, assign grade to "A". 
If it's between 80 and 89, assign it to "B". Otherwise, assign it to "C".
"""

"""score = int(input("Enter your test score: "))

if score >= 90:
    grade = "A"
    print(grade)
elif score >= 80:
    grade = "B"
    print(grade)
elif score >= 70:
    grade = "C"
    print(grade)"""

"""
Write a program that takes the user’s input for the current hour (0-23). 
If the hour is before 12, set time_of_day to "morning". 
If it's before 18, set it to "afternoon". Otherwise, set it to "evening".
"""

"""time = int(input("Enter current hour(0-23): "))

if time < 12:
    time_of_day = "morning"
    print(time_of_day)
elif time < 18:
    time_of_day = "afternoon"
    print(time_of_day)
elif time < 24:
    time_of_day = "evening"
    print(time_of_day)"""

"""
Create a program that asks the user about the weather 
(either "rainy", "sunny", or any other condition). 
If it’s "rainy", suggest wearing a raincoat. 
If it’s "sunny", suggest wearing sunglasses. 
Otherwise, suggest wearing regular clothes.
"""

"""
weather = str(input("Enter the weather(rainy, sunny, or other): "))

if weather == "rainy":
    print("I suggest wearing a raincoat.")
elif weather == "sunny":
    print("I suggest wearing sunglasses.")
elif weather == "other":
    print("I suggest wearing regular clothes.")
"""

"""
Write a program that asks the user to input their driving speed. 
If the speed is greater than 100, assign a traffic fine of $200. 
If it's between 81 and 100, assign a fine of $100. 
Otherwise, no fine is issued.
"""

"""
spd = int(input("Enter your driving speed: "))
if spd > 100:
    print("You are being fined $200!")
elif spd > 81:
    print("You are being fined $100!")
else:
    print("You are free to go.")
"""