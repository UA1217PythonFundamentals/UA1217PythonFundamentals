###### Task 1. Write a function that returns the largest number of two  numbers
# (use DocStrings documentation strings in the function).
def KY_max(a, b):
    """This function can be used to find the largest value and print it.
     Parameters:
    a (int or float): The first number.
    b (int or float): The second number."""
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return f"{a} value equals {b} value"
print(KY_max(7,3))
print(KY_max(2, 10.2))
print(KY_max(3,3.0))

z = KY_max(3,5)
print(z)


######Task 2. Task2. Write a program that calculates the area of a rectangle, triangle and circle
#(write three functions to calculate the area, and call them in the main program depending on the user's choice).
def KY_rectangle(a, b):
    """This function can be used to calculate the area of a rectangle using its length and width.
    Parameters:
    a (int or float): The length of the rectangle.
    b (int or float): The width of the rectangle."""
    area_rectangle = a * b
    return f"S rectangle = {area_rectangle}"
print(KY_rectangle(3.6,3))

def KY_triangle(a, h):
    """This function can be used to calculate the area of a triangle using its length and height.
        Parameters:
        a (int or float): The length of the triangle.
        b (int or float): The heights of the triangle."""
    area_triangle = (0.5 * a * h)
    round_triangle = round(area_triangle,3)
    return f"S triangle = {round_triangle}"
print(KY_triangle(13,5.8))


def KY_circle(r):
    """This function can be used to calculate the area of a circle using its r - circle radious and  π = 3.14159."""
    pi = 3.14159
    area_circle = (pi * r ** 2)
    return f"S circle = {area_circle}"
print(KY_circle(2))


##### Task3. Write a function that calculates the number of characters included in a given string
# input: "hello"
# output: {"h":1, "e":1,"l":2,"o":1}

given_string = input(str("Write something down: "))
dict_given_string = dict(())
for x in given_string:
    if x in dict_given_string:
        dict_given_string[x] += 1
    else:
        dict_given_string[x] = 1
print(dict_given_string)

