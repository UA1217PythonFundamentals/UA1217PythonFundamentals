# I. Jenny's secret message:

def greet(name):
    if name == "Johnny":
        return f"Hello, my love!"
    else:
        return f"Hello, {name}!"
    
# II. Simple: Find The Distance Between Two Points

import math
def distance(x1, y1, x2, y2): 
    dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return round(dis,2)

# III. No yelling!

def filter_words(st):
    seq=st.capitalize()
    message=' '.join(seq.split())
    pass
    return message


# IV.Convert a Number to a String!

def number_to_string(num):
    return str(num)


# V.Reversing Words in a String

def reverse(st):
    words=st.split()
    revers=' '.join(reversed(words))
    return revers


# VI. Reverse List Order

def reverse_list(l):
    return l[::-1]


# VII. Multiples of 3 or 5

def solution(number):
    return sum (i for i in range(1, number) if i % 3 == 0 or i % 5 == 0)


# VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg*fuel_left


# IX. Are You Playing Banjo?

import re
def are_you_playing_banjo(name):
    name_n=name.lower()
    if re.match(r'^r.*', name_n):
        return (f"{name} plays banjo")
    else:
        return (f"{name} does not play banjo")


# X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    if boolean == True:
        return ('Yes')
    if boolean == False:
        return ('No')
    

# XI. Counting sheep

def count_sheeps(sheep):
  result= sum( 1 for i in sheep if i == True)
  return result


# XII. Is this my tail?

def correct_tail(body, tail):
    return body[-1]==tail 

