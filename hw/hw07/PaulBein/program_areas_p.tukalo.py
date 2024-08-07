# Task2 program that calculates area of a rectangle, triangle and circle
PI = 3.14
def area_of_rectangle(a,b):
    S = a * b
    return S
def area_of_triangle(a,h):
    S = 0.5 * a * h
    return S
def area_of_circle(r):
    S = PI * r ** 2
    return S
# Case
while True:
    print('''Select the figure to calculate an area:
    1 - rectangle
    2 - triangle
    3 - circle
    q - to quit''')
    choise = input('Enter your choise: ')
    match choise:
        case 'q':
            break
        case '1':
            A = float(input('Enter side A: '))
            B = float(input('Enter side B: '))
            if A <= 0 or B <= 0:
                print('You must to enter positive values!')
                print('')
            else:
                print('Area of a rectangle:',round(area_of_rectangle(A,B),3))
                break
        case '2':
            A = float(input('Enter side: '))
            H = float(input('Enter height: '))
            if A <= 0 or B <= 0:
                print('You must to enter positive values!')
                print('')
            else:
                print('Area of a triangle:',round(area_of_triangle(A,H),3))
                break
        case '3':
            R = float(input('Enter radius: '))
            if R <= 0:
                print('You must to enter positive value!')
                print('')
            else:
                print('Area of a circle:',round(area_of_circle(R),3))
                break
        case _:
            print('Wrong choise!')
            print('')