# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# Find the distance between two points
import math
def distance(x1, y1, x2, y2):
    result = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
    return result


# No yelling!
def filter_words(st):
    st = st.casefold()
    start = st[0]
    st = st[1:]
    filtered = ' '.join(str(start.upper() + st).split())
    return filtered 


# Convert a number to a string
def number_to_string(num):
    return str(num)


# Reversing words in a string
def reverse(st):
    st = ' '.join(st.split()[::-1])
    return st


# Reverse list order
def reverse_list(l):
    return list(reversed(l))


# Multiplies of 3 or 5
def solution(number):
    if number < 0:
        return 0
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if fuel_left * mpg >= distance_to_pump else False


# Are you playing banjo?
def are_you_playing_banjo(name):
    if name.casefold().startswith('r'):
        return name + " plays banjo"
    return name + " does not play banjo"


# Convert boolean values to string "Yes" or "No"
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)


# Is this my tail?
def correct_tail(body, tail):
    return True if body.endswith(tail) else False