# Python philosophy Zen text
zen = """Beautiful is better than ugly.
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

# Separator between tasks
SEPARATOR="-"*79


# 03.1.a Find separately the number of occurances of the words 'better', 'never', and 'is':
better_count = zen.count("better")
never_count = zen.count("never")
is_count = zen.count("is")
print(f"The number of 'better' in Zen text is: {better_count}")
print(f"The number of 'never' in Zen text is: {never_count}")
print(f"The number of 'is' in Zen text is: {is_count}")
print(SEPARATOR)


# 03.1.b Display all text in uppercase:
print(zen.upper())
print(SEPARATOR)


# 03.1.c Replace oll occurances of 'i' with '&':
print(zen.replace("i", "&"))
print(SEPARATOR)


# 03.2.a Product of the digits in 4-digit natural number:
number = 1989
result = 1

for i in str(number):
    result *= int(i)

print(f"Product of {number} is: {result}")


# 03.2.b Number in reverse order:
reverse_number = str(number)[::-1]
print(f"Reversed number {number} is: {reverse_number}")


# 03.2.c Sort the numbers in ascending order:
sort_number = sorted(str(number))
sort_number = int("".join(sort_number))
print(f"Sorted number {number} is: {sort_number}")
print(SEPARATOR)


# 03.3 Interchange the values of two variables without using the third:
kit_salary = 1000
pes_salary = 100_000
print(f"Kit gets {kit_salary}$, Pes has {pes_salary}$")
kit_salary, pes_salary = pes_salary, kit_salary
print(f"Now Kit has {kit_salary}$, and Pes gets {pes_salary}$")