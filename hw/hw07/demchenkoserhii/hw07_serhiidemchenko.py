
# 07.1 Practical task

# task 1

def max_number(number1, number2):
    """Function that returns the largest number"""
    a = [number1, number2]

    print(max(a))

    return max(a)

max_number(5,8)

# task 2
PI = 3.14
def area_of_rectangle(width, height):
    a = width * height

    return a

def area_of_triangle(base, height):
    a = 0.5 * base * height

    return a

def area_of_circle(radius):
    a = PI * radius**2

    return a


def area_of_figure():
    while True:

        print("Choose a figure:")
        print("""Rectangle - 1
Triangle - 2
Circle - 3""")
        choise = input("Your choise: ")
        if choise == "1":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            print(f"Area of rectangle is: {area_of_rectangle(width, height)}")
            break
 
        elif choise == "2":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print(f"Area of triangle is: {area_of_triangle(base, height)}")
            break
            
        elif choise == "3":
            radius = float(input("Enter radius: "))
            print(f"Area of circle is: {area_of_circle(radius)}")
            break
        else:
            print("Error")
            break
        

area_of_figure()

# task 3

def number_of_characters(word):
    d_word = {}

    for i in word:
        if i in d_word:
            d_word[i] += 1
        else:
            d_word[i] = 1

    
    print(d_word)
    return d_word

number_of_characters("qwerty")

# 07.2 Practical task

# task 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# task 2

def distance(x1, y1, x2, y2):
    a = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    rounded_distance = round(a, 2)
    print(rounded_distance)

    return rounded_distance

distance(2, 2, 3, 4)

# task 3

def filter_words(st):
    lower_words = st.lower()
    capitalize_word = lower_words.capitalize()
    split_words = capitalize_word.split()
    words_with_spases = ' '.join(split_words)

    print(words_with_spases)

    return words_with_spases

filter_words("WOW this is REALLY          amazing")

# task 4

def number_to_string(num):
    string = str(num)
    print(string)

    return string
number_to_string(276)

# task 5

def reverse(st):
    split_w = st.split()
    split_w.reverse()
    result_text = ' '.join(split_w)
    print(result_text)

    return result_text

reverse("WOW this is REALLY          amazing")

# task 6

def reverse_list(l):
    l.reverse()
    print(l)

    return l

reverse_list([1, 2, 3, 4])

# task 7

def solution(number):
    if number < 0:
        return 0
    
    list = []
    for i in range(number):
        if i < 0:
            return 0
        if not i % 3 or not i % 5:
            list.append(i)
     
    print(sum(list))
    return sum

solution(10)

# task 8
    
def zero_fuel(distance_to_pump, mpg, fuel_left):

    if distance_to_pump >= mpg * fuel_left:
        
        return True
    else:
        return False


print(zero_fuel(50, 25, 2))

# task 9

def are_you_playing_banjo(name):
    if "R" in name[0]:
        print(f'{name} plays banjo')
    if "r" in name[0]:
        print(f'{name} plays banjo')
    else:
        print(f'{name} does not play banjo')


are_you_playing_banjo("rick")

# task 10

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

print(bool_to_word(False))  

# task 11

def count_sheep(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count

sheeps = [True, False, True, True, False]
print(count_sheep(sheeps))  

#task 12

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
    
print(correct_tail("tiger", "r"))


