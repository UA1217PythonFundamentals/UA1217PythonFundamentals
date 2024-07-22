from math import pi

# #Task 1: Write a fucntion that returns the largest number of two numbers

def the_largest_number(num1, num2):
    """Get the largest number between them, using the method max()"""
    result = max(num1, num2)
    print(f"The largest number between {num1} and {num2} is {result}.")


help(the_largest_number)
num1 = input("Enter 1st number:")
num2 = input("Enter 2nd number:")
the_largest_number(num1, num2)


#Task 2: Write a program that calculates the area of rectangle, triangle and cicle

def rectangle_calc():
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    result = width * length
    print(f"The area of rectangle with {length=} and {width=} is {result}.")

def triangle_calc():
    base=int(input("Enter the base of Triangle: "))
    height=int(input("Enter the height of Triangle: "))
    result = round((height * base) / 2)
    print(f"The area of triangle with {base=} and {height=} is {result}.")

def circle_calc():
    radius=int(input("Enter the radius of circle: "))
    result = round((pi * radius**2), 3)
    print(f"The area of circle with {radius=} is {result}.")

option=int(input("Choose an option: \n1. Calculate the area of rectangle. \n2. Calculate the area of Triangle.\n3. Calculate the area of circle.\n"))
if option == 1:
    rectangle_calc()
elif option == 2: 
    triangle_calc()
elif option == 3:
    circle_calc()
else:
    print("Error, unknown choice. Exiting the program..")
    

# Task 3: Write a function that calculates the number of characters included in given string

def count_char(word):
    char={}
    for i in word:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    
    return char

word = input("Enter the word: ")
print(count_char(word))