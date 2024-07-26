from Scalculation import KY_rectangle as rec, KY_circle as circ, KY_triangle as trian
def calc_rect():
    length = float(input("What is the lenght?: "))
    width = float(input("What is the width?: "))
    area_rec = rec(length, width)
    return f"S rectangle = {area_rec}"

def calc_trian():
    base = float(input("What is the base?: "))
    height = float(input("What is the height?: "))
    area_trian = trian(base, height)
    return f"S triangle = {area_trian}"

def calc_circ():
    r = float(input("What is the radious?: "))
    area_circ = circ(r)
    return f"S circle = {area_circ}"

def areas_calculation():
    area_to_calculate = input("What area you would like to calculate: 'rectangle', 'triangle' or 'circle'?: ").strip().lower()
    match area_to_calculate:
        case 'rectangle':
             return calc_rect()
        case 'triangle':
            return calc_trian()
        case 'circle':
            return calc_circ()
        case _:
            return "Invalid data. Please try again."

print(areas_calculation())