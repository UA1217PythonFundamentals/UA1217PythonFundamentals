# 1 task
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
# number of  words "better", "never" and "is" 
print("Numbers of 'better':", zen.count("better"))
print("Numbers of 'never':", zen.count("never"))
print("Numbers of 'is':", zen.count("is"))

# all text in uppercase
print(zen.upper())

# replace symbol
print(zen.replace("i","&"))


# 2 task
number=int(input("Enter 4 digit natural number:"))
number_str = str(number)
if len(number_str) != 4:
    print("The number is not 4 digit")

product = int(number_str[0]) * int(number_str[1]) * int(number_str[2]) * int(number_str[3])
print(f'The product of the {number} is: {product}')

revers_number = number_str[::-1]
print("Revers number:", revers_number)


sorted = "".join(sorted(number_str))
print("Sorted numbers:", sorted)

# Interchange the values of two variables without using the third variable.
value_1 = input("Value one:")
value_2 = input("Value two:")

value_1, value_2 = value_2, value_1

print("Value one after change:", value_1)
print("Value two after change:", value_2)