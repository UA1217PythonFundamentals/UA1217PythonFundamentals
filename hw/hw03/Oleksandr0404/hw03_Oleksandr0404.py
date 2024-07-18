# Python's philosophy Zen 
zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# Separator between tasks
SEPARATOR="-"*79

# Find number of occurrences of specific words
better_count = zen_of_python.count('better')
never_count = zen_of_python.count('never')
is_count = zen_of_python.count('is')

# Print results
print(f"Number of occurrences of 'better': {better_count}")
print(f"Number of occurrences of 'never': {never_count}")
print(f"Number of occurrences of 'is': {is_count}\n")
print(SEPARATOR)
# Display text in uppercase
print(zen_of_python.upper())
print(SEPARATOR)

# Replace all occurrences of "i" with "&"
replaced_text = zen_of_python.replace('i', '&')
print(replaced_text)
print(SEPARATOR)

# Given four-digit natural number
number = 1234  
# Convert the number to a string to easily access each digit
num_str = str(number)

# Calculate the product of the digits
product_of_digits = int(num_str[0]) * int(num_str[1]) * int(num_str[2]) * int(num_str[3])

# Reverse the number
reversed_number = num_str[::-1]

# Sort the digits in ascending order
sorted_digits = ''.join(sorted(num_str))

# Print results
print(f"Product of the digits: {product_of_digits}")
print(f"Number in reverse order: {reversed_number}")
print(f"Digits sorted in ascending order: {sorted_digits}")
print(SEPARATOR)

# Interchange the values of two variables without using the third:
a = 5
b = 10

a, b = b, a

# Print the results
print(f"Value of a after interchange: {a}")
print(f"Value of b after interchange: {b}")
