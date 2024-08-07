# Task1 function returned max of two numbers
print('-'*60)

def max_of_two(n1,n2):
    if n1 == n2:
        print("Numbers are equals")
    else:
        print("The largest number:",max(n1,n2))
# Checking the result
max_of_two(12,36)
max_of_two(0,-7)
max_of_two(3,3)

print('-'*60)

# Task3 function that calculates the number of characters included in given string
def number_of_char():
    dict = {}
    str = input('Enter string: ')
    for ch in str:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    print(dict)

number_of_char()