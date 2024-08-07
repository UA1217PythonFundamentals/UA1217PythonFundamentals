test_text = """
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


#Task1.1:
print("Amount of better: ", test_text.count("better"))
print("Amount of never: ", test_text.count("never"))
print("Amount of is: ", test_text.count("is"))


#Task1.2:
print(test_text.upper())


#Task1.3:
print(test_text.replace("i", ("&")))


#Task2.1:
number=6498
str_number=str(number)
result= int(str_number[0]) * int(str_number[1]) * int(str_number[2]) * int(str_number[3])
print(f"The product of four-digit number {number} is {result}.")


#Task2.2:
reverse=str(number)[::-1]
print(f"A four-digit number in reversed order: {reverse}")


#Task2.3:
sort="".join(sorted(str(number)))
print(f"Sorted numbers in ascending order: {sort}")


#Task3:
a=764
b=1564
print(f"Before exchange: a={a}, b={b}")
a, b = b, a
print(f"After exchange : a={a}, b={b}")