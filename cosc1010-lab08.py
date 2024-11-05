# Lucas Dillon
# UWYO COSC 1010
# Submission Date: 11/04/24
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to: NA
#


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def str_to_num(given):
    """Checks whether the given input is a number, and converts it to the correct type (int or float)."""
    while True:
        global negative
        negative = False
        if "-" in given:
            negative = True
            given = given.replace("-", "")

        if "." in given:
            given_split = given.split(".")

            for i in given_split:
                if not i.isnumeric():
                    return False

            if len(given_split) > 2:
                print("Too many periods!\n")
                return False

            elif given_split[0].isnumeric() and given_split[1].isnumeric():
                if negative:
                    return -float(given)
                else:
                    return float(given)

        elif "." not in given:
            if not given.isnumeric():
                return False
            
            else:
                if negative:
                    return -int(given)
                else:
                    return int(given)

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def point_slope(m, b, lower, upper):
    """A function taking in an input for m, b, and upper and lower bounds and outputting 
    a list of all values of y corresponding with given x integer values."""
    
    y = []
   
    m = str_to_num(m)
    b = str_to_num(b)
    lower = (str_to_num(lower))
    upper = str_to_num(upper)

    if (m == False) or (b == False) or (lower == False) or (upper == False):
        return False

    elif lower <= upper:
        for x in range(int(lower), int(upper) + 1):
            y.append((m*x) + b)
        return y


print("\nPoint Slope Inputs below:\n")
while True:
    m = input("Provide an m\n")
    if m == 'exit':
        break
    b = input("Provide a b\n")
    if b == 'exit':
        break
    lower = input("Provide a lower bound\n")
    if lower == 'exit':
        break
    upper = input("Provide an upper bound\n")
    if upper == 'exit':
        break

    answer = point_slope(m, b, lower, upper)

    if answer == False:
        print("One of these inputs is not a number.\n")
        continue
    else:
        print(answer)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_formula(a, b, c):
    a = str_to_num(a)
    b = str_to_num(b)
    c = str_to_num(c)

    if ((b**2) - (4*a*c)) < 0:
        return False
    x = (-b + ((b**2) - (4*a*c))**(1/2))/(2*a), (-b - ((b**2) - (4*a*c))**(1/2))/(2*a)
    return x

print("Quadratic formula inputs below:\n")
while True:
    a = input("Provide an a\n")
    if a == 'exit':
        break
    b = input("Provide a b\n")
    if b == 'exit':
        break
    c = input("Provide a c\n")
    if c == 'exit':
        break

    answer2 = quadratic_formula(a, b, c)

    if answer2 == False:
        print("One of these inputs is not a number or the answer involves imaginary numbers.\n")
    else:
        print(answer2)





