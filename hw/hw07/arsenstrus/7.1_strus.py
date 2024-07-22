#Task1
def larger_number(num1,num2):
    """"Function returns larger number"""
    if num1 > num2:
        return num1
    elif num2>num1:
        return num2
    else:
        return 0
#Task2
def area_of_rectangle(a,b):
    return a*b

def area_of_triangle(a,h):
    return 1/2*a*h

def area_of_circle(R):

    return R*3.14
print("For what type of figure you want to calculate area: Rectangle, Triangle, Circle")
figure=input()
figure=figure.lower()
match figure:

   case "circle":
       R =float(input("Input radius of the circle:"))
       print(f"The area of figure:{area_of_circle(R)}")
   case "triangle":
       a=input("Input  side a length:")
       h=input("Input height:")
       print(f"The area of figure:{area_of_triangle(a,h)}")
   case "rectangle":
       a = input("Input  side a length:")
       b = input("Input  side b length:")
       print(f"The area of figure:{area_of_rectangle(a, b)}")
   case _:
       print("ERROR")
#Task3
def count_char(word):
    char = {}
    for x in word:
        if x in char:
            char[x] += 1
        else:
            char[x] = 1

    return char

word=input("Enter the word: ")
print(count_char(word))