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
print (zen)

# 1.1 find separately the number of occurrences of the words "better", "never" and "is" in the given line

print ('The number of occurrences of the words "better" is', zen.count("better"))
print ('The number of occurrences of the words "never" is', zen.count("never"))
print ('The number of occurrences of the words "is" is', zen.count("is"))

# 1.2 you need to display all text in uppercase (all letters in uppercase)

print(zen.upper())

# 1.3 replace all occurrences of the symbol “i” with “&”

print(zen.replace("i", "&"))

# 2. A four-digit natural number is specified:

number = 2918

#input('Enter a four-digit natural number: ')

# 2.1 find the product of the digits of this number
number_str=str(number)
product = int(number_str[0]) * int(number_str[1]) * int(number_str[2]) * int(number_str[3])
print(f'The product of the {number} is: {product}')

# 2.2 write the number in reverse order
reverse_order = number_str[-1]+number_str[-2]+number_str[-3]+number_str[-4]
print(f'The reverse order of the {number} is: {reverse_order}')

# 2.3 in ascending order, you need to sort the numbers included in the given number
ascending_order = ''.join(sorted(number_str))

print("Number after sorting : " + str(ascending_order))

# 3. Interchange the values ​of two variables without using the third variable.

var1 = "Elena"
var2 = "Tyrsenko"
var1, var2 = var2, var1
print("var1:", var1)
print("var2:", var2)

