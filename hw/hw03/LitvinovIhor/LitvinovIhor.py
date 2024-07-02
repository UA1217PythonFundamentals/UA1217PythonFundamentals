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
print("="*10)


# 3.1.1
print(f'Number of "better": {zen.count("better")}')
print(f'Number of "never": {zen.count("never")}')
print(f'Number of "is": {zen.count("is")}')
print("="*10)

# 3.1.2

print(zen.upper())
print("="*10)

# 3.1.3

print(zen.replace("i","&"))
print("="*10)

# 3.2
number = 2812
conversion = str(number)
product = int(conversion[0]) * int(conversion[1]) * int(conversion[2]) * int(conversion[3])
print(f"Product of the digits of this numbers {number} is: {product}")
print("="*10)


# 3.2.1
print(f"Number in reverse order is: {conversion[::-1]}")
print("="*10)

# 3.2.2

print(f"Digits of number in ascending order of {number} is {sorted(conversion)}")
print("="*10)


# 3.3

user1 = "Ihor"
user2 = "Litvinov"
print(user1,user2)
user1,user2 = user2,user1
print(user1,user2)