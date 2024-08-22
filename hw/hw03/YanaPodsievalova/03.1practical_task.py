# 1
python_philosophy = """Beautiful is better than ugly.
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

#print(type(python_philosophy)) #self check

#number of "better", "never", "is"
sub1 = "better"
sub2 = "never"
sub3 = "is"
print(python_philosophy.count(sub1))
print(python_philosophy.count(sub2))
print(python_philosophy.count(sub3))

#all text in upper case

print(python_philosophy.upper())

#replace "i" with "&"
print(python_philosophy.replace("i","&"))

# 2 find the product of the digits of this number
number = 1234
conv = str(number)
digits = int(conv[0]) * int(conv[1]) * int(conv[2]) * int(conv[3])
print(digits)
#write the number in reverse order
reversed_number = conv[::-1]
print(reversed_number)
#in ASC
asc_number=''.join(sorted(reversed_number))
print(asc_number)

# 3 Interchange the values ​of two variables without using the third variable.
a = 'cat'
b = 'dog'
print(a + b)

a, b = a, b
print(a + b)
