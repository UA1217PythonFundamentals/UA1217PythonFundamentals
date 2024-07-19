from math import pi
def circle_calc():
    radius=int(input("Enter the radius of circle: "))
    result = round((pi * pow(radius,2)), 3)
    print(f"The area of circle with {radius=} is {result}.")