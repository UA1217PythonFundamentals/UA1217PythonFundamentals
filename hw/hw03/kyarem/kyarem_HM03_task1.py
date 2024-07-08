python_philosophy = str("""
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!""")

#-----------------
# TASK 1
#-----------------
#you need to write Python's philosophy in the string format
print(python_philosophy, type(python_philosophy))

#find seperately the number of occurences of the words "better", "never" and "is" in the given line
better_count, never_count, is_count = (python_philosophy.count("better"), python_philosophy.count("never"), python_philosophy.count("is"))
print(f"The number of times 'better' occurs: {better_count}")
print(f"The number of times 'never' occurs: {never_count}")
print(f"The number of times 'is' occurs: {is_count}")

#you need to display all text in uppercase
print(python_philosophy.upper())

#replace all occurences of the symbol "i" with "&"
print(python_philosophy.replace("i", "&"))

#-----------------
# TASK 2
#-----------------
#A four-digit natural number is specified:
#find the product of the digits of this number

specified_number = int(input("Enter a 4-digit natural number: "))
if specified_number > 9999:
    print("4-digit number is only allowed.")
    exit()

#-----------------
# approach 1
#-----------------
x1 = specified_number // 1000
x2 = specified_number // 100 - x1 * 10
x3 = specified_number // 10 - x2 * 10 - x1 * 100
x4 = specified_number - x3 * 10 - x2 * 100 - x1 * 1000
product_of_the_digits = x1 * x2 * x3 * x4
print(f"The product of digits of this number: {product_of_the_digits}")

# write the number in reverse order.
print(f"The reference order: {x4*1000+x3*100+x2*10+x1}")

#-----------------
# approach 2
#-----------------
converted_specified_number = str(specified_number)
print(f"The reference order: {converted_specified_number[::-1]}")

#in ascending order, you need to sort the numbers included in the given number
sorted_order = list(converted_specified_number)
sorted_order.sort()
print(f"The asc.order of the numbers: {sorted_order}")

#-----------------
# TASK 3
#-----------------
#Interchange the values of two variables without using the third variable.
a = 20
b = 30
a = a + b
b = a - b
a = a - b
print(f" a = {a},b = {b}")