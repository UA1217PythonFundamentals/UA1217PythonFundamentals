# def my_first_func():
#     print("start my_first_func")
#     a = 20
#     print(f"\t{a=}")
#     print("end my_first_func")

# my_first_func()
# my_first_func()
# my_first_func()

# print(my_first_func)

# f = my_first_func

# # f()
# print(sum([1,2,3]))

# def sum(a, b):
#     print(f"a+b={a+b}")

# print(sum)
# sum(1, 2)
# print(sum([1,2,3]))

# help(sum)
# print(sum.__doc__)


# def f(a, b):
#     """todo func f
#     return None
#     """
#     result = a+b
#     return result
# help(f)
# print(f.__doc__)

# # f()


# def f(a, b):
#     print(f"{a}+{b}={a+b}")

# r = f(5, 9)
# print(f"{r=}")


# def f(a, b):
#     print(f"{a}+{b}={a+b}")
#     result = a+b
#     return result
#     print("end")

# r = f(9, 17)

# print(f"{r=}")


# def my_print(text):
#     print(text)
# # my_print()#TypeError: my_print() missing 1 required positional argument: 'text'
# # my_print(1,2,3)#TypeError: my_print() takes 1 positional argument but 3 were given
# my_print("Liubomyr")

# def my_print(text, count):
#     print(f"{text=} {count=} ",text*count)
# # my_print()#TypeError: my_print() missing 2 required positional arguments: 'text' and 'count'
# # my_print(1)#TypeError: my_print() missing 1 required positional argument: 'count'
# my_print("Liubomyr", 3)
# my_print(3, "Liubomyr")


# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)

# # print_info()#TypeError: print_info() missing 1 required positional argument: 'name'
# print_info("Liubomyr")
# print_info("Liubomyr", 38)


# def print_info(name, age=18, city):#SyntaxError: parameter without a default follows parameter with a default
# print("Name: ", name)
# print("Age: ", age)
# print("City: ", city)

# def print_info(name,  city, age=18):
# # def print_info(name, age=18, city="Lviv"):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("City: ", city)

# print_info("Liubomyr", "Odesa")
# print_info(99, "Liubomyr", "Odesa")


# def print_info(name, city, age=18, country="Ukrain"):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Country:", country, "City: ", city)

# # print_info("Liubomyr", "Odesa")
# # print_info(99, "Liubomyr", "Odesa")


# print_info(age=99, name="Liubomyr", city="Odesa")


# def f(r1, r2, *args, d1=1, d2=22, **kwargs):
#     print(f"{r1=}  {r2=} {args=} {d1=} {d2=} {kwargs=}")
# def f(r1, r2, *a, d1=1, d2=22, **k):
#     print(f"{r1=}  {r2=} {a=} {d1=} {d2=} {k=}")


# f(1, 2)
# f(1, 2, 3)
# f(1, 2, d1=3)
# f(1, 2, d1=3, d2=99)
# f(1, 2, d2=99)
# f(1, 2, 3, 4, 5, 6, d1=999, dd=888)
# f(1, 2, 3, 4, 5, 6, d1=999, dd=888, ff=11)
# f((3, 4, 5), 2, (3, 4, 5), 6, d1=999, dd=888, ff=11)

# l = (1, 2, 3, 4, 5, 6)
# f(l[0], l[1], l[2], l[3], l[4], l[5])
# f(*l)
# d ={
#     "d1": 88,
#     "d11": 888
# }
# f(1,2, d1=d["d1"], d11=d["d11"])
# f(1,2, **d)

# def f():
#     t = 10
#     return t

# c = f()
# print(c)
# print(t)

# glob = 'global'

# def f():
#     loc = "local"
#     print(loc, glob)

# f()

# def f():
#     loc = "local"
#     glob = 30
#     print(loc, glob)
# f()
# print(f"{glob=}")


# def f():
#     global glob
#     loc = "local"
#     glob = 30
#     print(loc, glob)
# f()
# print(f"{glob=}")


# def f():
#     loc = "local"
#     def f2():
#         nonlocal loc
#         g = "f2"
#         loc = 20
#         print(f"{g=} {loc=}")
#     f2()
#     print(f"{loc=}")


# f()

# def f(n):
#     for i in reversed(range(0, n+1)):
#         print(i)
# f(5)

# def rf(n):
#     if (n < 0):
#         return
#     print(n)
#     rf(n-1)

# import sys
# sys.setrecursionlimit(2000)
# rf(5)


# l = [1, 2, 3, [2, 3, 4, 5], [111, [11, 1, 1, 2]]]


# def f(a, level = 0):
#     print(level*"\t", a)
#     s = 0
#     for i in a:
#         if type(i) in (list, tuple):
#             s += f(i, level+1)
#         else:
#             s += i
#     return s

# print(f(l))


# def factorial(in_data):
#     print(in_data, end="*")
#     if in_data == 1:
#         print()
#         return 1
#     return in_data * factorial(in_data-1)
# print(factorial(3)) 
# print(factorial(8)) 


f = lambda a,b,c: a+b+c
# print((lambda a,b,c: a+b+c)(1,3,4))
# print(f(1,2,3))

def f(a,b,c):
    return a+b+c
print(f(1,2,3))
f = 10


l =["9", 1,2,3, "123"]
l.sort(key=lambda x: int(x) if type(x) is str else x)
print(l)
def lll(x):
    if type(x) is str:
        return -int(x)
    else:
        return -x
l.sort(key=lll)
print(l)