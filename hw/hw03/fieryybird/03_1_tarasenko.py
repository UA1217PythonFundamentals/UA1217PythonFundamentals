zen = '''
Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!
'''

def separator():
    separator = "-"*55
    print(separator)

# Find separately the number of occurrences of the words
print(f'Number of "better": {zen.count("better")}')
print(f'Number of "never": {zen.count("never")}')
print(f'Number of "is": {zen.count("is")}')
separator()

# Display all text in uppercase
print(zen.upper())
separator()

# Replace all occurrences of the symbol “i” with “&”
print(zen.replace("i","&"))
separator()

# Find the product of the digits of four-digit natural number
number = 1993
digits = str(number)

product = int(digits[0]) * int(digits[1]) * int(digits[2]) * int(digits[3])
print(f'The product of the {number} is: {product}')
separator()

# Write the number in reverse order
reverse_order = digits[::-1]
print(f'The reverse order of the {number} is: {reverse_order}')
separator()

# Sort the digits of number in ascending order
ascending_order = "".join(sorted(digits))
print(f'{number} in ascending order is: {ascending_order}')
separator()

# Interchange the values ​of two variables without using the third variable.
var_1 = "Soft"
var_2 = "Serve"
print(var_1+var_2)

var_1, var_2 = var_2, var_1
print(var_1+var_2)



