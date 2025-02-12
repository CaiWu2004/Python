import random


pseudo_random_line_slop = random.randint(-5, 5)
pseudo_random_line_y_intercept = random.randint(0, 10)
print("Welcome to Drawing Parallels! Test whether your line is parallel to the line f(x)=",pseudo_random_line_slop, "x+", pseudo_random_line_y_intercept)

slope = int(input("Enter a slope:"))

y_intercept = int(input("Enter a y-intercept:"))

if slope == pseudo_random_line_slop:
    if y_intercept != pseudo_random_line_y_intercept:
        print("Your line f(x) = ", slope, "x+", y_intercept, "is parallel to the line f(x)=", pseudo_random_line_slop, "x+", pseudo_random_line_y_intercept)
    else:
        print("Your line f(x) =", slope, "x+", y_intercept, "is not parallel to the line f(x)=", pseudo_random_line_slop, "x+", pseudo_random_line_y_intercept,)
else:
    print("Your line f(x) = ", slope, "x+", y_intercept, "is not parallel to the line f(x)=", pseudo_random_line_slop, "x+", pseudo_random_line_y_intercept,"because their the same!")
