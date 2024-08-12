#Jenny's secret message
greeting_messsage = lambda name: "Hello, my sweetheart!" if name == "Johny" else f"Hello, {name}."

#Find The Distance Between Two Points
point_distance = lambda x1,y1,x2,y2: round(((x1 - x2)**2 + (y1 - y2)**2)**0.5,2)

#No yelling!
capital_prop_spac = lambda string: " ".join(string.split()).capitalize()

#Convert a Number to a String
convert_numb_to_str = lambda number: str(number)

#Reversing Words in a String
revers_word = lambda word: " ".join(word.split()[::-1])

#Reverse list order
revers_list = lambda list: list[::-1]

#Multiples of 3 or 5
sum_of_numb = lambda numb: 0 if numb < 0 else sum(i for i in range(numb) if i % 3 == 0 or i % 5 == 0)

#Will you make it?
posib_to_pump = lambda dist_pump, fuel: True if fuel * 25 >= dist_pump else False

#Are You Playing Banjo?
banjo_player = lambda name: name + " plays banjo" if name[0] == "B" or name[0] == "b" else name + " does not play banjo"

#Convert boolean values to strings 'Yes' or 'No'.
bool_to_str = lambda bool_var: 'Yes' if bool_var == True else 'No'

#Counting sheep...
count_sheep = lambda array: f'There are {sum(i for i in array if i == True)} sheeps, not {len(array)}'

#Is this my tail?
right_tail = lambda animal,tail: True if tail == animal[len(animal)-1] else False



