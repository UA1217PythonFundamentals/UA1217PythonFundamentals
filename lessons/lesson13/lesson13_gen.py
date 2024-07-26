# # l = [x*x for x in range(5)]
# # print(l)
# # l = {x*x for x in range(5)}
# # print(l)
# # l = {x:x*x for x in range(5)}
# # print(l)

# # l = (x*x for x in range(5))
# # print(l)

# # l = ["1", '-3', "7"]
# # ll = list(map(int, l))
# # print(ll)
# # ll = [int(x) for x in l]
# # print(ll)
# # ll = filter(lambda n: int(n)>0, l)
# # print(list(ll))
# # from functools import reduce

# # def a_add_b(a, b):
# #     print(f"{a=} {b=} {a+b=}")
# #     return a+b
# # print(reduce(a_add_b, [47,11,42,13]))
# # print(reduce(a_add_b, [47,11,42,13], -99))

# # s = "Hello!!!"
# # print(s)
# # it = iter(s)
# # print(it)
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # # print(next(it)) #StopIteration

# # def cycle(it, func):
# #     try:
# #         it = iter(it)
# #     except:
# #         pass
# #     try:
# #         element = next(it)
# #     except StopIteration:
# #         return
# #     func(element)
# #     cycle(it, func)

# # cycle(s, print)


# # class MyNumbers:
# #     def __iter__(self):
# #         self.a = 1
# #         return self
# #     def __next__(self):
# #         x = self.a
# #         self.a += 1
# #         if self.a > 100:
# #             raise StopIteration()
# #         return x
    

# # myclass = MyNumbers()
# # myiter = iter(myclass)
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # for i in MyNumbers():
# #     print(i)


# def my_gen(n):
#     print("start my_gen")
#     i = 0
#     while True:
#         print("end my_gen while start")
#         if i >= n:
#             break
#         yield i
#         print("end my_gen while end")
#         i +=1
#     print("end my_gen")


# # print(">"*20)
# # g = my_gen(5)
# # print(">"*20)
# # print(g)
# # print(">"*20)
# # print(next(g))
# # print(">"*20)
# # print(next(g))
# # print(">"*20)
# # print(next(g))
# # print(">"*20)
# # print(next(g))
# # print(">"*20)
# # print(next(g))
# # print(">"*20)
# # print(next(g))
# # print(">"*20)

# n = 10
# print(f"{n=}")
# l = list(range(n))
# print(l.__sizeof__())
# g = my_gen(n)
# print(g.__sizeof__())

# n = 10**3
# print(f"{n=}")
# l = list(range(n))
# print(l.__sizeof__())
# g = my_gen(n)
# print(g.__sizeof__())

# n = 10**5
# print(f"{n=}")
# l = list(range(n))
# print(l.__sizeof__())
# g = my_gen(n)
# print(g.__sizeof__())

# n = 10**7
# print(f"{n=}")
# l = list(range(n))
# print(l.__sizeof__())
# g = my_gen(n)
# print(g.__sizeof__())

# g = (x*x for x in range(1,10))
# print(g)
