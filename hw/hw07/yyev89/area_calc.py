# Task 2: program that calculates the area of rectangle, triangle, and circle
PI = 3.14

def triangle_area(b, h):
    '''Calculates area (a) of triangle with base (b) and height (h)'''
    a = 1/2 * b * h
    return a

def rectangle_area(l, w):
    '''Calculates area (a) of rectangle with lenght (l) and width (w)'''
    a = l * w
    return a

def circle_area(r):
    '''Calculates area (a) of circle with radius (r) and PI'''
    a = PI * r**2
    return a


welcome_msg = '''
Welcome to area calculation program.
Please, select a figure (0 to quit):
1) triangle
2) rectangle
3) circle
'''
while True:
    print(welcome_msg)
    selector = int(input('Please enter [1-3]: '))
    match selector:
        case 0:
            break
        case 1:
            base = float(input('Enter base (b): '))
            heigh = float(input('Enter heigh (h): '))
            triangle = round(triangle_area(base, heigh), 2)
            print(f'Area of triangle is: {triangle}')
        case 2:
            lenght = float(input('Enter lenght (l): '))
            width = float(input('Enter width (w): '))
            rectangle = round(rectangle_area(lenght, width), 2)
            print(f'Area of rectangle is: {rectangle}')
        case 3:
            radius = float(input('Enter radius (r): '))
            circle = round(circle_area(radius), 2)
            print(f'Area of circle is: {circle}')
        case _:
            print('Wrong selection, please try again')