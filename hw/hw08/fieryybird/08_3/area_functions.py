from math import pow,pi

rectangle_area = lambda length, width: round(length * width, 2)
triangle_area = lambda base, height: round(0.5 * base * height, 2)
circle_area = lambda radius: round(pow(radius,2) * pi,2)
