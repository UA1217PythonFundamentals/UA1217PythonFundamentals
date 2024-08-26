#Task 1
def numbers(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1
print(numbers(3,7))

#Task 3

def count(x):
    char_count = {}
    for char in x:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = "hello"
print(count(input_string))