# Task 1.

def largest_number(n1,n2):
  '''Return the largest number, take 2 arguments.'''
  if isinstance(n1, (int, float)) and isinstance(n2, (int, float)):
    if n1 > n2:
      return(n1)
    elif n1 < n2:
      return(n2)
    elif n1 == n2:
      return('equal')
  else:
    return('Invalid datatype.')
  

print(largest_number(-5,10.2))

# Task 2. 

circle_area = lambda radius: round((3.14 * radius ** 2), 2)
rectangle_area = lambda length, width: round((length * width), 2)
triangle_area = lambda a, b, c, s: round(((s * (s - a) * (s - b) * (s - c)) ** 0.5), 2)

def get_values(prompt):
    '''Split given input string into float values.'''
    return map(float, input(prompt).split())

def calculate_area(figure_type):
    '''Calculate the area of a chosen figure using lambda functions.'''
    match figure_type:
        case 'rectangle':
            length, width = get_values("Enter the length and width of the rectangle: ")
            return(rectangle_area(length, width))
        case 'triangle':
            a, b, c = get_values("Enter the lengths of the 3 sides of the triangle: ")
            semi_perimeter = (a + b + c) / 2
            return(triangle_area(a, b, c, semi_perimeter))
        case 'circle':
            radius, = get_values("Enter the radius of the circle: ")
            return(circle_area(radius))


figure_type = input('Provide the figure type to calculate its area: \n')
result = calculate_area(figure_type)
print(f'Area is: {result}')

# Task 3.

def number_of_characters(str):
  '''Return the number of characters included in the given string.'''
  converted_string = str.lower()
  result = {}
  for i in converted_string:
    if i != ' ':
      result[i] = converted_string.count(i)
  return(result)


str = input("Enter any text and I'll calculate number of characters: \n")
print(number_of_characters(str))

