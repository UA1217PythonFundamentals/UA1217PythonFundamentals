#Homework 1
#Working text
text1 = """
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
#All letters in uppercase
print(text1.upper())

#"Better", "never", "is" count 
print("better =", text1.count('better'))
print("never = ", text1.count('never'))
print("is = ", text1.count('is'))

#Replace all occurrences "i" with "&"
print(text1.replace('i', '&'))

#Homework 2.1

a = int(input("Enter b ="))
b = str(a)

if len(b) != 4:
    print("Invalid number")
    
print(int(b[0])*int(b[1])*int(b[2])*int(b[3]))

#Homework 2.2
user_info = input("Enter a four digit number: ")
if len(user_info) !=4:
    print("invalid number")

user_list = str(user_info)[::-1]
print(user_list)

#Homework 2.3
user_info = input("Enter a four digit number: ")
if len (user_info) !=4:
    print("Invalid number")
user_list = list(str(user_info))
user_list = sorted(user_list)
print(*user_list, sep='')

#Homework 3
val1 = input("Enter val1: ")
val2 = input("Enter val2: ")
val1, val2 = val2, val1
print("val1 =", val1)
print("val2 =", val2)