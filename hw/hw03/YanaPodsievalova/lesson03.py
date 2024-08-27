#bool true/false
b = True
print(b)
b = False
print(b)
# int має обмеження, нвбір цілиз чисел
i = 10**9999
import sys
sys.set_int_max_str_digits(10000)
print(i)
#float = 12.5 дефолтно 14 знаків після коми
#list, tuple, str, set, frozenset, dict - представляють набір елементів
#list[], set, dict - змінні
#tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
#str = “My name is …”
#set = set('qwerty') => set(['e', 'q', 'r', 't', 'w', 'y'])
#frozenset = frozenset('qwerty')
#dict = {'name': 'john',‘id':6734, ‘role': ‘admin'}

a = 10
print(a, id(a))

a = "20"
print(a, id(a))
a +="0"
print(a, id(a))

# list
x = [1, 2, 3, 4]
x.append(99) #додали\модифікували об'єкт 
print(x, id(x))

m = 1
print (m, type(m))


m = [1, 2.2, "134"]
print (m, type(m))

a = 1.123456778 #округлення
print(round(a, 3))


my_name = "Yana Podsievalova" #snake_case

a = 1 + 2 + 3 + 4 \
+ 5
print(a)

a = ("test1"
     "test2"
    "test3")
print(a); print(a)

#declaring
name = "Yana"

x ,y, z = 1, 2, 3
print(x, y, z)

#assing mult values
info = ("Yana", 34, "Kyiv")
name, age, city = info
print(name, age, city)

x = 1
y = 1
z = 1

x = y = z = 1

s1 = "hot"
s2 = "dog"
print(s1 + s2)


str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())

first_name = "television"
hobby = "homer"
tmp = first_name
first_name = hobby
hobby = tmp
print(f"T{first_name[1:3]} likes to watch {hobby[4:]}")

str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub,4))

str1 = 'Welcome'
print(str1*2)

print("John" > "Jhon")
print("Emma" < "Emm")


print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

p, q, r = 10, 20, 30
print(p, q, r)



str1 = """Ault'Kelly"""
print(str1)

str1 = 'Ault\'Kelly'
print(str1)

#str1 = 'Ault\\'Kelly'
#print(str1)

value = 36 / 4 * (3 + 2) * 4 + 2
print(value)


value_one = 5 ** 2
value_two = 5 ** 3
print(value_one)
print(value_two)


print(type({}) is set)

variable_1 = 1
variable_2 = 3
variable_3 = "3"
print(variable_1 + variable_2 + variable_3)