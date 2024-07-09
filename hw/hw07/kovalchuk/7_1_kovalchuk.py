# Task1. Write a function that returns the largest number of two numbers (use DocStrings documentation strings in the function).

# Task2. Write a program that calculates the area of a rectangle, triangle, and circle (write three functions to calculate the area. And call them in the main program depending on the user's choice).

# Task3. Write a function that calculates the number of characters included in a given string

# input: "hello"
# output: {"h":1, "e":1, "l":2, "o":1}


# Task1. Write a function that returns the largest number of two numbers (use DocStrings documentation strings in the function).


def return_bigger(a, b):
    if a>b:
        return a
    else: 
        return b
    

# Task2.  Write a program that calculates the area of a rectangle, triangle, and circle (write three functions to calculate the area. And call them in the main program depending on the user's choice).

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return base * height * 0.5

def circle_area(radius):
    return 3.14 * radius * radius


def main():
    

    while True:
        enter_condition = input("What do u want calculate?: \n 1. Rectangle\n 2. Triangle\n 3. Circle\n 4.Exit\n")
        if enter_condition =="1" :
            length = float(input("Enter rectangle length: "))
            width = float(input("Enter rectangle width: "))
            area = rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")

        elif enter_condition=="2":
            base = float(input("Enter base of triangle : "))
            height = float(input("Enter triangle height: "))
            area = triangle_area(base, height)
            print(f"The area of the triangle is: {area}")

        elif enter_condition=="3":
            radius = float(input("Enter radius of circle: "))
            area = circle_area(radius)
            print(f"The area of the triangle is: {area}")
        elif enter_condition=="4":
            print("Exit")
            break
        else:
            print("Wrong number, try again: ")

if __name__ == "__main__":
    main()


# Task3. Write a function that calculates the number of characters included in a given string

# input: "hello"
# output: {"h":1, "e":1, "l":2, "o":1}


def calculates (str):
    char_count={}
    for char in str:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

enter_str = input("Enter text: ")
result = calculates(enter_str)
print(result)