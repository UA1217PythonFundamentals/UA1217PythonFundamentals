#TASK 1
def largest_number (num1, num2):
# Returns the largest of two numbers.
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    elif num1 == num2:
        return ('equel')
    else:
        return ('not valid datatype')

print(largest_number(10,-8.2))