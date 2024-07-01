# 1. Python philosophy in the string format. 
#import this 
python_philosophy="""
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

# 1.1 find separately the number of occurrences of the words - "better", "never" and "is" in the given line 12
list_of_lines=python_philosophy.split(".")
given_line=str(list_of_lines[12]).split()
print(given_line)
count_better = given_line.count('better')
count_never = given_line.count("never")
count_is = given_line.count('is')
print('''Number of occurrences of the word 'better':''', count_better)
print('''Number of occurrences of the word 'never':''' ,count_never)
print('''Number of occurrences of the word 'is':''' ,count_is)


# 1.2 Python philosophy in uppercase (all letters in uppercase)
up=python_philosophy.upper
print(up())

# 1.3 replace all occurrences of the symbol “i” with “&”
rp=python_philosophy.replace("i", "&")
print(rp)

# 2 2124 - the four-digit natural number
# 2.1 find the product of the digits of this number
x=2124
y=list(str(x))
a, b, c, d=int(y[0]), int(y[1]), int(y[2]), int(y[3])
z=a*b*c*d
print(z)

# 2.2.1 write the digits of number in reverse order
print(str(y[::-1]))

# 2.2.2 write the number in reverse order
reverse_number=int("".join(y[::-1]))
print("Reverse number of 2124:", reverse_number)

# 2.3 in ascending order, you need to sort the numbers included in the given number
asc=list(str(x))
asc.sort()
print("""The numbers included in the number "2124" sorted in ascending order: """, asc)

# 3. Interchange the values ​of two variables without using the third variable.
ab='happy'
bc='you'
print('Two variables:', ab,bc)
ab, bc = bc, ab
print('Interchanged variables:', ab,bc)           
