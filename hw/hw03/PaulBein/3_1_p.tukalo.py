# Zen philosophy text
zen = '''Beautiful is better than ugly.
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

#Find separately the numbers of occurrences of the words
print("The count of words 'better':",zen.count("better"))
print("The count of words 'never':",zen.count("never"))
print("The count of words 'is':",zen.count("is"))
print("-"*65)

#Display all text in uppercase
print(zen.upper())
print("-"*65)

#Replace all occurrences of the symbol "i" with "&"
print(zen.replace("i","&"))
print("-"*65)

#Four-digit natural number
number = 7838
print("Four-digit number:",number)
digits = str(number)
print("Product of the digits of this numbers:",int(digits[0])+int(digits[1])+int(digits[2])+int(digits[3]))
print("Number in reverse order:", digits[::-1])
print("Digits of number in ascending order:","".join(sorted(digits)))
print("-"*65)

#Interchange the values of two variables without using the third variable
a = "Paul"
b = "Bein"
print(a,b)
a,b = b,a
print("Reverse>>")
print(a,b)