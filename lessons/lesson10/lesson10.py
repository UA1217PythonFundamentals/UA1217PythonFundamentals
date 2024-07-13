import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
# class ClassName():
#     pass

# class ClassName:
#     pass

# # class ClassName(object):# in python 2.4+
# #     pass


# print(ClassName)

# c1 = ClassName()
# print(c1)


# class A:
#     ci = "class"
#     cm = ["class"]

#     def __init__(self, ii="instans", im=["instans"]):
#         print("init:", self, ii, im)
#         self.ii = ii
#         self.im = im

# c1 = A()
# c2 = A("test1", [1,2,3])
# print(c1.ci, c1.cm, c1.ii, c1.im)
# print(c2.ci, c2.cm, c2.ii, c2.im)

# c1.ii = 10
# c1.im.append(10)
# c2.im.append(88)
# c2.cm.append("temp")


# print(c1.ci, c1.cm, c1.ii, c1.im)
# print(c2.ci, c2.cm, c2.ii, c2.im)

# print(dir(A))
# print()
# print(A.__dict__)
# print()
# print(dir(c1))
# print()
# print(c1.__dict__)


# class Human:
#     def __new__(cls, *args, **kwargs):
#         print(f"__new__ {cls}")
#         instance = super(Human, cls).__new__(cls)
#         # instance.a = "A"
#         return instance
#     def __init__(self, name=None, age=None, gerden=None):
#         print(f"__init__ {self} {self.__dict__}")
#         self.name = name
#         self.age = age
#         self.gerden = gerden
#     def __del__(self):
#         print(f"delete {self}")

#     def print_details(self):
#         print(f"Name {self.name}")
#         print(f"Age {self.age}")
#         print(f"Gerden {self.gerden}")

#     def from_city(self, city):
#         return f"{self.name} from {city}"


# person1 = Human("Liubomyr", 38, "m")
# person2 = Human("Olha", 1, "w")

# print(person1, type(person1) is Human, type(person1))
# print(person2, type(person1) is Human)

# print(person1.print_details)
# person1.print_details()
# person2.print_details()
# print(person1.from_city("Lviv"))
# print(person2.from_city("Odesa"))

# # print_details()#NameError: name 'print_details' is not defined


# def func_print_details(person):
#     print(f"Name {person.name} Age {person.age} Gerden {person.gerden}")


# func_print_details(person1)
# func_print_details(person2)

# s = sum
# print(s([1,2,3,4,5,]))

# f = Human.from_city
# print(Human.from_city)
# print(f)
# print(f(person1, "ifrank"))
# temp = lambda a: a
# temp.name = "TEMP"
# print(f(temp, "ifrank"))

# Human.print = func_print_details

# person1.print()

# del person2

# print(">>End<<"*10)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} y:{self.y} "

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):  # self + other
        temp = Point()
        if isinstance(other, Point):
            temp.x = self.x + other.x
            temp.y = self.y + other.y
        elif type(other) is int:
            temp.x = self.x + other
            temp.y = self.y + other
        return temp

    def __lt__(self, other):
        w1 = (self.x**2 + self.y**2) ** 0.5
        w2 = (other.x**2 + other.y**2) ** 0.5
        return w1 < w2

    def __eq__(self, value) -> bool:
        return self.x == value.x and self.y == value.y


# p1 = Point(1,-3)
# p2 = Point(10, 15)
# t = str(p1)
# print(f"{t=}")
# print(p1)
# print(p2)
# print([p1,p2])
# p3 = p1 + p2
# print(p3)
# p4 = p1 + 9
# print(p4)

# from random import randint

# points = [Point(randint(-10, 10), randint(-10, 10)) for _ in range(10)]
# print(points)
# points.sort()
# print(points)
# p10 = Point(11, 11)
# p11 = Point(11, 11)
# print(p10 == p11)
# print(p10 == p1)


# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         super().__init__(x, y)
#         # self.x = x
#         # self.y = y
#         print("Point3D__init__", self.__dict__)
#         self.z = z
#     def __str__(self):
#         return f"x: {self.y} x: {self.y} z: {self.z}"
#     def __repr__(self):
#         return super().__repr__()[:-1] + f",{self.z})"

# p31 = Point3D()
# print(p31.__dict__)
# print(p31)
# from random import randint
# points = [Point3D(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(10)]
# print(points)

# class A:
#     def f(self):
#         print("A f()")
# class B(A):
#     def K(self):
#         print("B k()")
# class C(A):
#     def g(self):
#         print("C g()")
# class D(B):
#     def k(self):
#         print("D k()")
# class E(B):
#     def g(self):
#         print("E g()")
# class F(C, B): pass
# class G(D, E, F): pass
# g = G()
# g.k()
# g.f()
# g.g()
# print(G.__mro__)
# class G( F, D, E): pass
# g = G()
# g.k()
# g.f()
# g.g()
# print(G.__mro__)

# class A:

#     def __init__(self):
#         self.a = 1

#     def f(s):
#         print(s, type(s))

#     @classmethod
#     def c(cls):
#         print(cls, type(cls))

#     @staticmethod
#     def s():
#         print("text")

# a = A()
# a.f()
# # A.f()#TypeError: A.f() missing 1 required positional argument: 'self'
# A.f(a)

# print(A, type(A))
# a.c()
# A.c()

# a.s()
# A.s()


# class AAA:
#     def __init__(self) -> None:
#         self.a = 1
#         self._a = 2
#         self.__a = 3
#     def __str__(self):
#         return f"{self.a=} {self._a=} {self.__a=}"
#     def __f(self):
#         print(f"{self.a=} {self._a=} {self.__a=}")
# a = AAA()
# print(a.a)
# print(a._a)
# # print(a.__a)#AttributeError: 'A' object has no attribute '__a'. Did you mean: '_a'?
# print(a._AAA__a)#AttributeError: 'A' object has no attribute '__a'. Did you mean: '_a'?
# print(a)
# a._AAA__f()


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"x:{self.__x} y:{self.__y} "

    def __repr__(self):
        return f"({self.__x},{self.__y})"

    def get_x(self):
        print("get_x")
        return self.__x

    def set_x(self, x):
        print("set_x")
        if (type(x) in (float, int)):
            self.__x = int(x)
        else:
            print("Error")
    x = property(get_x, set_x)

    @property
    def y(self):
        print("get_y")
        return self.__y
    @y.setter
    def y(self, y):
        print("set_y")
        self.__y = y


p = Point(-999, -999)

print(p.get_x())
# p.__x = 25

p.set_x("15")
p.set_x(15)
# print(p.get_x())
print(p)
print(p.x)
p.x = "adsaf"
p.x = 23
print(p)
print(p.y)
p.y = 88
print(p)