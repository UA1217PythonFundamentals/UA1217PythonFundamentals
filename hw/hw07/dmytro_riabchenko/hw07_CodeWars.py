#Task1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# Task2
import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)


# Task3
def filter_words(st):
    words = st.split()
    filtered_sentence = ' '.join(words).lower().capitalize()
    return filtered_sentence


# Task4
def number_to_string(num):
    return str(num)


# Task5
def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


# Task6
def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]


# Task7
def solution(number):
    if number < 0:
        return 0
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# Task8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False


# Task9
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# Task10
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"


# Task11
def count_sheeps(sheep):
    return sheep.count(True)


# Task12
def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if sub == tail:
        return True
    else:
        return False
