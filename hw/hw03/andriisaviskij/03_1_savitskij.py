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


# #1.1: Counting words "better", "never", "is"
print("Amount of better: ", zen.count("better"))
print("Amount of never: ", zen.count("never"))
print("Amount of is: ", zen.count("is"))


# #1.2: Display Zen text in uppercase
print(zen.upper())


# #1.3: Replacing all occurrences os the symbol "i" with "&"
print(zen.replace("i",("&")))
print("-----"*30)

# #2.1:Product of Four-digit number: 
number=1543
strnum=str(number)
result=int(strnum[0])*int(strnum[1])*int(strnum[2])*int(strnum[3])
print(f"The product of four-digit number {number} is {result}.")


# #2.2: Reverse order of Four-digit number:
reverse=str(number)[::-1]
print(f"A four-digit number in reversed order: {reverse}")


# #2.3: Sort numbers included in ascending order:
sort="".join(sorted(str(number)))
print(f"Sorted numbers in ascending order: {sort}")
print("-----"*30)

#3: interchanging values of two variables w/o 3rd variable
a=15
b=4215
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After: a={a},b={b}")