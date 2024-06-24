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

# task 1.1

print("Number of \"better\":", zen.count("better"))
print("Number of \"never\":", zen.count("never"))
print("Number of \"is\":", zen.count("is"))
# task 1.2

print(zen.upper())
# task 1.3

replace_text = zen.replace("i", "&")
print(replace_text)

# task 2.1
number = 6637

number_str = str(number)
num_list = list(number_str)
product = int(num_list[0])*int(num_list[1])*int(num_list[2])*int(num_list[3])

print(f"Product of {number} is {product}")

# task 2.1

reverse = num_list[3]+num_list[2]+num_list[1]+num_list[0]

print(f"Revers of {number} is {reverse}")

#task 2.2







