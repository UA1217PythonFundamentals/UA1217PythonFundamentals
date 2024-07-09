philosophi = '''
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
#Line to separate tasks
separator = "-"*25

#Task 1
print("\n",separator, "Task 1", separator)

#Task 1.1
print ("Better count: ", philosophi.count("better"))
print ("Never count: ", philosophi.count("never"))
print ("Is count: ", philosophi.count("is"))
print(separator)

#Task 1.2
print("Python's philosophy in uppercase:","\n",philosophi.upper())
print(separator)

#Task 1.3
print("Text after replasing:","\n",philosophi.replace("i", "&"))

#Task 2
print("\n",separator, "Task 2", separator)

#Task 2.1
number = 1965
print("Number is:", number)

digits = str(number)

print("Product of numbers is:", int(digits[0])*int(digits[1])*int(digits[2])*int(digits[3]))
print(separator)

#Task 2.2
reverse_number = digits[::-1]
print("Number in reverse order:", reverse_number)
print(separator)

#Task 2.3
ascending_order = sorted(digits)
print("Digits in ascending order:", ascending_order)

#Task 3
print("\n",separator, "Task 3", separator)

a=19
b=65
print("Digits before interchanging:", "\n", "First:", a, "\n", "Second:", b)
a, b = b, a
print("Digits after interchanging:", "\n", "First:", a, "\n", "Second:", b)
