a = """The Zen of Python, by Tim Peters

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one-- and preferably only one --obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than *right* now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!
"""

# Task 1.1
number_better = a.count("better")
number_never = a.count("never")
number_is = a.count("is")
print(f'The word "better" occurs {number_better} times, \t the word "never" occurs {number_never} times, \t the word "is" occurs {number_is} times, in The Zen of Python.')

# Task 1.2
d = a.upper()

# Task 1.3
p = d.replace("I", "&")
print(p)

# Task 2.1
digit=4321
x = str(digit)
z0 = int(x[0])
z1 = int(x[1])
z2 = int(x[2])
z3 = int(x[3])
product = z0 * z1 * z2 * z3
print("The product of the digits is", product)

# Task 2.2
m1=x[::-1]
m2=int(m1)
print(m2, type(m2))

# Task 2.3
as1=sorted(x)
print(as2)
