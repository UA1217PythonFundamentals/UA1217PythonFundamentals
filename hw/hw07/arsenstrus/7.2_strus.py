#Task1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
#Task2
def distance(x1, y1, x2, y2):
    result=round(pow(pow(x1-x2,2)+pow(y1-y2,2),0.5),2)
    return result
#Task3
def filter_words(st):
    words = st.split()
    filtered_sentence = ' '.join(words).lower().capitalize()
    return filtered_sentence
#Task4
def number_to_string(num):
   return str(num)
#Task5
def reverse(st):
    words = st.split()

    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence
#Task6
def reverse_list(l):
    reverse_l = l[::-1]
    return reverse_l
#Task7
def solution(number):
    result = 0
    if number < 0:
        return 0
    while number > 3:
        number = number - 1
        if number % 3 == 0:
            result += number
        elif number % 5 == 0:
            result += number
    return result

#Task8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump>mpg*fuel_left:
        return False
    else:
        return True
#Task9
def are_you_playing_banjo(name):
    answer = ""
    if name[0] == 'R' or name[0] == 'r':
        answer = name + " plays banjo"
        return answer
    else:
        answer = name + " does not play banjo"
        return answer

#Task10
def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'
#Task11
def count_sheeps(sheep):
    answer = 0
    for x in sheep:
        if x:
            answer += 1
    return answer

#Task12
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False