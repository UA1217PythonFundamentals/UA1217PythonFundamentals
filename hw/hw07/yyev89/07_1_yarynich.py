# Task1: write a function that returns the largest number of two numbers
def largest(a, b):
    '''Function returns the largest of two provided numbers as arguments,
    or "equal" in case when numbers are equal   
    '''
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "equal"


# Task 3: write a function that calculates the number of each character in given string
def char_count(word):
    '''Function counts the number of each character in provided string
    and returns it in the form of dictionary 
    '''
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result