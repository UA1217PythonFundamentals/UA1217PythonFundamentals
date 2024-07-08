from area_functions import rectangle_area, triangle_area, circle_area


def get_values(prompt):
    '''Split input string into float values.'''
    return map(float, input(prompt).split())


def calculate_area(figure_type):
    '''Calculate the area of a chosen figure.'''
    match figure_type:
        case 'rectangle':
            length, width = get_values("Enter the length and width of the rectangle: ")
            return(rectangle_area(length, width))
        case 'triangle':
            base, height = get_values("Enter the lengths of the 3 sides of the triangle: ")
            return(triangle_area(base, height))
        case 'circle':
            radius, = get_values("Enter the radius of the circle: ")
            return(circle_area(radius))
        
figure_type = input('Provide the figure type to calculate its area: \n')
print(f'Area is: {calculate_area(figure_type)}')
