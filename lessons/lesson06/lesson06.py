# ## List

# l = []
# print(type(l), l)

# l = [1, "a", [1,2,3], True]
# print(type(l), l)

# l = list()
# print(type(l), l)

# # l = list(213) #TypeError: 'int' object is not iterable
# l = list((1, "a", [1,2,3], True))
# print(type(l), l)
# l = list("SoftServe")
# print(type(l), l)

# l = ['S', 'o', 'f', 't', [1, 2, 3, (None, "a", True) ]]
# print(l[0])
# print(l[4])
# print(l[4][2])
# print(l[4][3])
# print(l[4][3][-1])
# print(l[2:4])
# print(l[::2])
# print(l + l)
# print(l*4)

# l[3] = l[3].upper()
# print(l)
# print(l[2].upper())#not change
# l[4].append("test")
# print(l)

# print([1,2,3] == [1,2,3])
# print([1,2,3] == [3,2,1])

# l = ['S', 'o', 'f', 't']
# print(dir(list))
# print([methods for methods in dir(list) if not methods.startswith("_")])

# l.append(1)
# print(l)
# l.append("Serve")
# print(l)
## clear
# print(id(l))
# l.clear()
# print(l)
# print(id(l))

# l = []
# print(l)
# print(id(l))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9, l1, l2]
# print(l3)
# l1[-1] = 33
# l2[1] = 55
# print(l3)
# print(l3[4] is l2)
# l1.clear()
# l2 = []
# print(l3)
# print(l3[4] is l2)

## copy
# t = l
# print(t, t is l)
# t[0] = 111
# print(l)

# t = l.copy()
# print(t, t is l)
# t[0] = 111
# print(l)
# print(t)


# l = ['S', 'o', 'f', 't', ["S", "e", "r", "v", "e"]]

# # t = l.copy()
# t = l[:]
# t[0] = 111
# t[-1][1] = "E"
# print(l)
# print(t)
# from copy import deepcopy

# tt = deepcopy(t)
# print(tt)
# t[-1][1] = "EEEE"
# print(l)
# print(t)
# print(tt)
# l = ['S', 'o', 'f', 't', ["S", "e", "r", "v", "e"]]
# print(l)
# print(l.count("S"))
# print(l.count("Ss"))
# print(l.count(["S", "e", "r", "v", "e"]))


# # l.extend(1) #TypeError: 'int' object is not iterable
# print(l)
# l.append("Serve")
# l.extend("Serve")
# print(l)
# print(l.index("e"))
# print(l.index("e", l.index("e") + 1 ))
# print(l.index("e", 8 ))
# # print(l.index("e", 8 ,9)) #ValueError: 'e' is not in list
# print(l.index("e"))
# # print(l.index("eу")) #ValueError: 'eу' is not in list
# l.insert(1, "temp")
# print(l)
# l.insert(111, "temp1")
# l.insert(-111, "temp2")
# print(l)


# p = l.pop()
# print(p, l)
# p = l.pop(2)
# print(p, l)
# p = l.remove("e")
# print(p, l)
# p = l.reverse()
# print(p, l)
# p = reversed(l)
# print(list(p), l)
# l = ['S', 'o', 'f', 't']
# l.sort()
# print(l)
# l = ['S', 'o', 'f', 't', ["S", "e", "r", "v", "e"]]

# def my_e(element):
#     if type(element) is list:
#         return str(element)
#     return element

# l.sort(key=my_e )
# print(l)
# t = [1,4,2,3,7,4]
# f = [1,"",2,3,0,4]
# tt = sorted(t)
# print(t, tt)
# print(all(t), all(f))
# print(any(t), any(f), any([0,None,False]))

# l = ['S', 'o', 'f', 't', ["S", "e", "r", "v", "e"]]

# e = enumerate(l)
# print(list(e))

# for i in l:
#     print(i)


# for i in range(len(l)):
#     print(i, l[i])

# for i in enumerate(l):
#     print(i)

# a, b = 1, 2

# for i, v in enumerate(l):
#     print(i, v)


# l = []
# for i in range(10):
#     if not i % 2:
#         print(i)
#         l.append(i**2)

# print(l)

# t = [i**2 for i in range(10) if i % 2]
# print(t)
# t = [int(i) for i in "1234567"]
# print(t)


### tuple

# t = ()
# print(type(t), t)

# t = (1,2,"Soft")
# print(type(t), t)
# t = (1)
# print(type(t), t)
# t = ("1")
# print(type(t), t)
# t = ("1",)
# print(type(t), t)
# t = tuple()
# print(type(t), t)

# t = tuple("SoftServe")
# print(type(t), t)

# print(t[0])
# # t[0] = "R" #TypeError: 'tuple' object does not support item assignment
# print(t[:3])

# print([methods for methods in dir(tuple) if not methods.startswith("_")])


# s = "jbhsnalkdvbkdlsbfkjlgmndifl"

# l = list(s)
# t = tuple(s)
# print(l.__sizeof__(), t.__sizeof__())

# s = "jbhsnalkdvbkdlsbfkjlgmndifl"*10000

# l = list(s)
# t = tuple(s)
# print(l.__sizeof__(), t.__sizeof__())


# l = list(range(10))
# t = tuple(range(10))
# print(l.__sizeof__(), t.__sizeof__())

# # s = "jbhsnalkdvbkdlsbfkjlgmndifl"*10000

# l = list(range(10**5))
# t = tuple(range(10**5))
# print(l.__sizeof__(), t.__sizeof__())

# ### set
# s = {} #<class 'dict'> {}
# s = set()
# print(type(s), s)
# s = set("vfdsjlkabfvkjsdhbvkjdslhfndgjksadbfgkfdslfbvkdlfbndklsfbnksldjfbvkdsjfglkrdfg")
# print(type(s), s)
# s = {'f', 's', 'b', 'a', 'r', 'l', 'k', 'h', 'g', 'j', 'v', 'd', 'n'}
# print(type(s), s)
# # s = {[1,2,3]} #TypeError: unhashable type: 'list'
# # s = {(1,2,3)}  #TypeError: unhashable type: 'list'

# # s = {(1,2)}
# # print(s)
# print("s" in s)
# print("ss" in s)
# s.add("sss")
# print(s)
# print(s.pop())
# # print(s.pop(1))#TypeError: set.pop() takes no arguments (1 given)
# print(s)
# s.remove('g')
# # s.remove('gg')#KeyError: 'gg'
# print(s)
# print("gg".__hash__())
# print((1,2,3).__hash__())


# # class A:
# #     def __hash__(self) -> int:
# #         return "pass"
# # a = A()
# # print(a.__hash__())
# s.update("216546516")
# s.update([1,2,3,4])
# print(s)
# print([methods for methods in dir(set) if not methods.startswith("_")])

# for i in s:
#     print(i)
# s = set("vfdsjlkabfvkjsdhbvkjdslhfndgjksadbfgkfdslfbvkdlfbndklsfbnksldjfbvkdsjfglkrdfg")
# print(sorted(s))


### dict

d = {}
print(type(d), d)
d = {1: "value", "key1": 12}
print(type(d), d)

d = dict()
print(type(d), d)
# d = dict("jkdsbgkd")#ValueError: dictionary update sequence element #0 has length 1; 2 is required
d = dict([[1,2], [3,"value"], ("key", "test")])
print(type(d), d)

d = dict(enumerate("jkdsbgkd"))
print(type(d), d)

d = {1: "value", "key1": 12, 1: "111"}
print(type(d), d)

print(d[1])
print(d["key1"])
d["my_key"] = 12
print(d)
print("my_key" in d)
d["my_key"] = "212"
print(d)
# print(d[2]) #KeyError: 2

print([methods for methods in dir(dict) if not methods.startswith("_")])

print(d.fromkeys([1,'key1', 33]))
print(d.fromkeys([1,'key1', 33], 55))

print(d["key1"])
print(d.get("key1"))
print(d.get("key12222"))
print(d.get("key12222", -999))
print(d.pop("key1"))
print(d)
print(d.popitem())
print(d)
d.update({1: "value", "key1": 12})
print(d)
d.update(enumerate("jkdsbgkd"))
print(d)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)


d1 = {1: 'k', 'key1': 12, 0: 'j', 2: 'd', 3: 's', 4: 'b', 5: 'g', 6: 'k', 7: 'd'}
d2 = {1: 'k', 'key1': 12, 0: 'j1', 2: 'd2', 33: 's', 4: 'b', 53: 'g', 63: 'k3', 7: 'd'}

d3 = d1.copy()
for key in d2.keys():
    if key in d3:
        if d3[key] != d2[key]:
            d3[key] = [d3[key], d2[key]]
    else:
        d3[key] =  d2[key]
print(d3)

f = open("f.txt")
# print(f.readline())
for line in f:
    print(line)