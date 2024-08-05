
from area_functions import area_circle, area_rectangle, area_triangle

def validate_input(prompt):
    '''Validates user input for numeric values only,
    which are greater than 0'''
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print('Please enter number greater than 0')
        except ValueError:
            print('Invalid input, please enter a number')
            continue

def calculate_area():
    while True:
        selector = validate_input('Please select [1-4]: ')
        match selector:
            case 1:
                base = validate_input('Enter base: ')
                height = validate_input('Enter height: ')
                triangle = round(area_triangle(base, height), 2)
                print(f'Area of triangle is: {triangle}')
            case 2:
                length = validate_input('Enter length: ')
                width = validate_input('Enter width: ')
                rectangle = round(area_rectangle(length, width), 2)
                print(f'Area of rectangle is: {rectangle}')
            case 3:
                radius = validate_input('Enter radius: ')
                circle = round(area_circle(radius), 2)
                print(f'Area of circle is: {circle}')
            case 4:
                print('Thanks for using this program. Bye')
                break
            case _:
                print('Wrong selection, please try again')


welcome_msg = '''
Welcome to the area calculation program.
Please select option:
1) triangle
2) rectangle
3) circle
4) quit
'''

if __name__ == "__main__":
    print(welcome_msg)
    calculate_area()
