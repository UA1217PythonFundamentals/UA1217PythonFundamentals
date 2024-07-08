# 1. You need to write Python's philosophy in the string format:

zen = """
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
"""
print(zen)

# - find separately the number of occurrences of the words "better", "never" and "is" in the given line

print("The number of word 'better' is:", zen.count('better'))
print("The number of word 'never' is:", zen.count('never'))
print("The number of word 'is' is:", zen.count('is'))

# - you need to display all text in uppercase (all letters in uppercase)

print(zen.upper())

# - replace all occurrences of the symbol “i” with “&”

print(zen.replace('i','&'))

# 2. A four-digit natural number is specified:

number = input('Print a four-digit natural number: ')

# - find the product of the digits of this number

product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print("The product of the digits of this number is:", product)

# - write the number in reverse order

reverced_number = number[3] + number[2] + number[1] + number [0]
# or reverced_number = number[::-1]
print("The number in reverse order:", reverced_number)

# - in ascending order, you need to sort the numbers included in the given number

print("Sortted numbers:", ''.join(sorted(number)))

# 3. Interchange the values of two variables without using the third variable.

a = input('Print "a": ')
b = input('Print "b": ')

a,b = b,a

print('a =', a)
print('b =', b)