

# def decor(funk):
#     def inner():
#         print(">>>>decor")
#         funk()
#         print("<<<<decor")
#     return inner
# def print_1():
#     print("1111")

# print_1 = decor(print_1)
# def print_2():
#     print("2")
# print_2 = decor(print_2)

# print_1()
# print_1()
# print_1()
# print_1()
# print_2()

# @decor
# def print_3():
#     print("3")

# print_3()

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner

# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner

# @percent
# @percent
# @percent
# @star
# @star
# def print_sum(a,b, c=0):
#     print(a+b+c)

# print_sum(1,2)
# print_sum(1,2,5)


# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         result = func(*args, **kwargs)
#         print("*" * 30)
#         return result
#     return inner


# @star
# def sum(a,b, c=0):
#     return a+b+c
# r1 = sum(1, 2)
# r2 = sum(1, 2, 7)
# print(r1)
# print(r2)
# def my_dec(s, count=10):
#     def decor(func):
#         def inner(*args, **kwargs):
#             print(s * count)
#             result = func(*args, **kwargs)
#             print(f"{args=}, {kwargs}, {func.__name__}, {result}")
#             print(s * count)
#             return result
#         return inner
#     return decor

# @my_dec("*")
# def sum(a,b, c=0):
#     return a+b+c


# @my_dec("=", 30)
# def div(a,b):
#     return a/b
# r1 = div(1, 2)
# r2 = sum(1, 2, 27)
# r2 = sum(1, 4, 7)
# r2 = sum(1, 5, 71)
# print(r1)
# print(r2)


def my_dec(s):
    def decor(func):
        def inner(*args, **kwargs):
            result = f"{s} {func(*args, **kwargs)} {s}"
            return result
        return inner
    return decor
@my_dec("*")
def f(text):
    return text

print(f("met"))
print(f("met"))
@my_dec("<>")
def f(text):
    return text
print(f("met"))

print(f("met"))
