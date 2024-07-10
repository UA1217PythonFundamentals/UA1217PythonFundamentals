# 1) Jenny's secret message
greet = lambda name: 'Hello, my love!' if name == 'Johnny' else f'Hello, {name}!'

# 2)  Find The Distance Between Two Points
distance = lambda x1, y1, x2, y2: round((((x2 - x1)**2 +(y2 - y1)**2)**0.5),2)

# 3) No yelling!
filter_words = lambda st: " ".join(st.split()).capitalize()

# 4) Convert a Number to a String
number_to_string = lambda num: str(num)

# 5)  Reversing Words in a String
reverse = lambda st: " ".join(st.split()[::-1])

# 6) Reverse List Order
reverse_list = lambda l: l[::-1]

# 7) Multiples of 3 or 5
solution = lambda number: 0 if number < 0 else sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# 8) Will you make it?
zero_fuel = lambda distance_to_pump, mpg, fuel_left: True if mpg * fuel_left >= distance_to_pump else False

# 9) Are You Playing Banjo?    
are_you_playing_banjo = lambda name: f'{name} plays banjo' if name[0] == 'R' or name[0] == 'r' else f'{name} does not play banjo'
    
# 10) Convert boolean values to strings 'Yes' or 'No’
bool_to_word = lambda boolean: 'Yes' if boolean == True else 'No'
    
# 11) Counting sheep
count_sheeps = lambda sheep: sheep.count(True)

# 12) Is this my tail?
correct_tail = lambda body,tail: True if body[-1]==tail else False

