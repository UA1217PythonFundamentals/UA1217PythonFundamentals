# b = True
# print(b)
# b = False
# print(b)
# i = 10
# print(i)
# i = 9**9999
# import sys
# sys.set_int_max_str_digits(10000)
# print(i)

# a = 10
# print(a, id(a))

# a = 20
# print(a, id(a))

# a = "20"
# print(a, id(a))
# a += "0"
# print(a, id(a))

# x = [1,2,3,4]
# print(x, id(x))
# x.append(99)
# print(x, id(x))
# a = 1
# print(a, type(a))
# a = "1"
# print(a, type(a))
# a = [1, 2.2, "34"]
# print(a, type(a))

# a = 1.123456789

# print(a)
# print(round(a, 8))
# print(round(a, 5))
# print(round(a, 2))
# my_name = "Liubomyr"


# a = 1 + 2 + 3 \
#     + 3 + 8 \
#     -7
# print(a)

# a = (1 + 2 + 3
#     + 3 + 8
#     -7)
# print(a)

# a = ("test1"
#     "test2"
#     "test3")
# print(a); print(a); print(a)

# for i in range(3):
#     print(i)
#     print(i)


# # string name;
# name = "Liubomyr"

# x, y, z = 1, 2, 3
# print(x, y, z)

# info = ("Liubomyr", 38, "Lviv")
# name, age, city = info
# print(name, age, city)
# x = 1
# y = 1
# z = 1
# x = y = z = 1


# a = 10
# b = 20
# c = a
# print(a, b, c)
# a = 11
# print(a, b, c)
# a = [1,2,3]
# b = a
# print(a, b)
# a.append(55)
# b[2] = 88
# print(a, b)
# print(id(a))
# print(id(b))


# PI = 3.14

# print(PI)

# PI = 99
# print(PI)


# x = 0b10001
# print(x)
# x = 0o21
# print(x)
# x = 17
# print(x)
# x = 0x11
# print(x)

# x = 100000000000
# print(x)
# x = 100_000_000_000
# print(x)


# f = 1.1
# print(f)
# f = .1
# print(f)
# f = 1.
# print(f)

# f = 17.58
# print(f)
# f = 1758e-2
# print(f)
# f = 1.758e1
# print(f)


# b = True
# print(b, type(b))
# b = False
# print(b, type(b))

# print(1 == True)
# print(0 == True)
# print(0.1 == True)
# print(0 == False)

# a = [1,2,3]
# b = [1,2,3]
# c = a

# print(a is b, a == b)
# print(a is c, a == b)


# l = [1, "12", 1.5, None]
# for i in l:
#     print(i, type(i))

# print(l)
# l[0] = 999
# print(l)
# t = (1, "12", 1.5, None)
# print(t)
# # t[0] = 999 #TypeError: 'tuple' object does not support item assignment

# s = {1,32,312,3,21,3,2,21,3,213,21,3,12,3,21,3,21,3,21,3,213,21,3,21,3,21,3,12,3}
# print(s)
# print(32 in s)
# print(5 in s)

# d = {12: "value_12", "key": None}

# print(d)
# print(d[12])
# print(d["key"])
# # print(d[0]) #KeyError: 0

# a = 1
# print(a, type(a) is int, type(a))
# a = 1.1
# print(a, type(a) is int, type(a))

# line = "123456"
# print(line, type(line))
# x = int(line)
# print(x, type(x))
# # x = int("abc") #ValueError: invalid literal for int() with base 10: 'abc'

# x = int("abc", 16)
# print(x)
# # x = int("abc", 38) #ValueError: int() base must be >= 2 and <= 36, or 0

# f = float(x)
# print(f, type(f))

# f = float("12.4")
# print(f, type(f))

# s = set("gdjbfjgnbvsjgdbdvhcvjdbfvjnvdfj")
# print(s)


# for i in range(260):
#     print(i, "-", chr(i))

# for i in "GVBJ%&^**UB VYUIxvxvd":
#     print(i, "-", ord(i))


# t = """text"""
# t = '''text'''
# print(2**8)
# t = u"gvbdshvbkc"
# print(t)
# text = "hello, Liubomyr"
# print(text)
# print("="*10)
# text = "hello,\nLiubomyr"
# print(text)
# print("="*10)
# text = "hello11111111111,\rLiubomyr"
# print(text)
# print("="*10)
# text = "hello\tLiubomyr"
# print(text)
# for i in range(1,99, 12):
#     print(f"{i}\t{i**3}\t{i**9}")


# # text = 'I'm Liubomyr'
# text = "I'm Liubomyr"
# text = 'I\'m Liubomyr'

# template = "%s is %d years old. Your sallary is %.9f $"
# name = "John"
# age = 23
# salary = 999.99
# print(template %  (name, age, salary))
# age = 99
# print(template %  (name, age, salary))


# template = "{} is {} years old. Your sallary is {:.3f} $"
# print(template.format(name, age, salary))

# template = "{name1} {name1} is {age1} years old. Your sallary is {:.3f} $"
# print(template.format(salary, name1=name, age1=age ))


# text = f"{name} is {age + 20} years old. Your sallary is {round(salary, 2)} $"
# print(text)


# text = 10
# import sys
# sys.set_int_max_str_digits(10_000)
# while True:
#     print(text)
#     text = text*99


# text = "SoftServe"

# print(text[0],text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8] )
# print(text[-1], text[-2], text[len(text)-3] )
# print(text[2:5])
# print(text[:5])
# print(text[4:])
# print(text[1:7:3])
# print(text[::3])

# m = [ method for method in dir(str) if not method.startswith("_")]
# print(m)
# text = "here is a complete list of all the built-in. methods to work with strings in Python"
# print(text.capitalize())
# print(text.center(100))
# print(text.count("i"))
# print(text.title())
# print(text.replace("et", "XXX"))


# text = 10
# import sys
# sys.set_int_max_str_digits(10_000)
# while True:
#     print(text.__sizeof__())
#     text = text*99

from datetime import datetime

# print(t)
# t = datetime.now()
# 1
