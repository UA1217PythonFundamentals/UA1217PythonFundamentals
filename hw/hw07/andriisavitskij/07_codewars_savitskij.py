#Task 1: Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)


#Task 2: Distance between two points:
# def distance(x1, y1, x2, y2):
#     # Your code here
#     result = ((x2-x1)**2 + (y2-y1)**2)**0.5   #w/o using math lib
#     return round(result,2)


#Task 3: No yelling!
# def filter_words(st):
#     st=st.capitalize()
#     if "    " in st:
#         st = st.replace("    ", " ")
#     if st.endswith(" "):
#         st = st[:-1]
#     return st


#Task 4: Convert a number to a string:
# def number_to_string(num):
#     num = str(num)
#     return num


#Task 5: Reversing words in a string
# def reverse(st):
#     st = " ".join(st.split()[::-1])
#     return st


#Task 6: Reverse List Order
# def reverse_list(l):
#     'return a list with the reverse order of l'
#     return l[::-1]


#Task 7: Multiples of 3 or 5
# def solution(number):
#     l=[]
#     for i in range(0, number):
#         if i % 3 == 0 or i % 5 == 0:
#             l.append(i)
#     result = sum(l)
#     return result


#Task 8: Will you make it?
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if fuel_left * mpg >= distance_to_pump:
#         return True
#     else:
#         return False
#     #Happy Coding! ;)


#Task 9: Are You Playing Banjo?
# def are_you_playing_banjo(name):
#     # Implement me!
#     if name.startswith("r") or name.startswith("R"):
#         res = (f"{name} plays banjo")
#     else:
#         res = (f"{name} does not play banjo")
#     return res


#Task 10: Yes or no
# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"


#Task 11: Counting Sheep
# def count_sheeps(sheep):
#     c = 0
#     for i in sheep:
#         if i == True:
#             c += 1
#         else:
#             pass
#     return c


#Task 12:Is this my tail?
# def correct_tail(body, tail):
#     if body.endswith(tail):
#         return True
#     else:
#         return False