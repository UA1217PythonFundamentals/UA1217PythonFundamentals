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
print("="*15)


# Find separately the number of occurrences of the word
print(f'Number of "better": {zen.count("better")}')
print(f'Number of "never": {zen.count("never")}')
print(f'Number of "is": {zen.count("is")}')
print("="*15)


# Display all text in uppercase
print(zen.upper())
print("="*15)

# Replace all occurrences of the symbol “i” with “&”
print(zen.replace("i","&"))
print("="*15)

#Product of four-digit number
number = 2156
conversion = str(number)
product = int(conversion[0]) * int(conversion[1]) * int(conversion[2]) * int(conversion[3])
print(f"The product of the {number} is: {product}")
print("="*15)


# Write the number in reverse order
print(f"The reverse order is: {conversion[::-1]}")
print("="*15)


# Sort the digits of number in ascending order
print(f"The ascending order of {number} is {sorted(conversion)}")
print("="*15)


# Interchange the values ​of two variables without using the third variable.
name1 = "Dmytro"
name2 = "Riabchenko"
print(name1 + name2)

name1, name2 = name1, name2
print(name1 + name2)
