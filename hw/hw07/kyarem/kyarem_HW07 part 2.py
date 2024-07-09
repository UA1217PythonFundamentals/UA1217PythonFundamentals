#1. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


#2. Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dist_calculate = (x2 - x1)**2 + (y2 - y1)**2
    rounded_dist = round((dist_calculate)**0.5, 2)
    return rounded_dist
print(distance(4,2,4,1))


#3. No yelling!
def filter_words(st):
    st = str(st)
    x = st.capitalize()
    return ' '.join(x.split()) #' '.join(x.split()) splits the string into words and then joins them with a single space.
print(filter_words('hoommmG               hjkkf llll'))


#4. Convert a Number to a String!
def number_to_string(num):
    num = str(num)
    return num
print(type(number_to_string(123)))


#5. Reversing Words in a String
def reverse(st1):
    st1 = st1.split()   # Розділяємо рядок на список слів
    rst1 = st1[::-1]    # Перевертаємо список слів
    reversed_string = ' '.join(rst1) # Об'єднуємо перевернутий список слів у рядок з одним пробілом між словами
    return reversed_string
print(reverse("Hello world"))


#6. Reverse List Order
def reverse_list(l):
    l.reverse()
    return l
print(reverse_list([1, 2, 3, 4]))


#7. Multiples of 3 or 5
def solution(number):
    x = 0
    if number < 0:
        return 0
    total_sum = 0
    for x in range(number):
       if x % 3 == 0 or x % 5 == 0:
           total_sum += x
    return total_sum

print(solution(1000))


#8. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return "True"
    else:
        return "False"
print(zero_fuel(56,2,25))


#9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print(are_you_playing_banjo("rob"))


#10. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean is True:
        return 'Yes'
    else:
        return 'No'
print(bool_to_word('false'))


#11. Counting sheep
def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x:
            count += 1
    return count
print(count_sheeps([True, True, True, False, True,  True,  True,  True,True,  False, True,  False,True,  False, False, True,True,  True,  True,  True,
  False, False, True,  True]))


#12.Is this my tail?
def correct_tail(body, tail):
    if body[-1] == tail[0]:
        return True
    else:
        return False
print(correct_tail("cat", "frog"))


