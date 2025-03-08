#2 Formatting Fun

#2a
intro = ("My name is {name}, and I'm {age} years old.").format(name='Oleg', age=18)
print(intro)

#2b

steps = ("I walked a total of {} steps this weekend.").format(2400 + 5630 + 1094)
steps = (f"I walked a total of {2400 + 5630 + 1094} steps this weekends")
print(steps)

#2c

exam =("I averaged a {} across all my exams!").format((65+85+80)/3)
print(exam)
exam = (f"I averged a {(65+85+80)/3} across all my exams!")
print(exam)


#2d

walk = ("Last week it was {Wk1_temp} degrees, and this week its {Wk2_temp} degrees. That's a 6 degree difference!").format(Wk1_temp=81,Wk2_temp=75)
print(walk)