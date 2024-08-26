class Animal:
    def __init__(self,name,species,legs):
        self.name,self.species,self.legs = name,species,legs
class Mammal(Animal):
    def __init__(self,name,species,legs):
        super().__init__(name,species,legs)
    def make_sound(self):
        return "Roar"
class Bird(Animal):
    def __init__(self,name,species,legs):
        super().__init__(name,species,legs)
    def make_sound(self):
        return "Squank"
class Reptile(Animal):
    def __init__(self,name,species,legs):
        super().__init__(name,species,legs)
    def make_sound(self):
        return "Hiss"

animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]
for animal in animals:
    print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")
#lion = Mammal("Lion","Mammal",4)
#print(lion.name,lion.species,lion.legs,lion.make_sound())
print('-'*50)

class BankAccount:
    def __init__(self,__account_number,__account_holder,balance):
        self.account_number,self.account_holder,self.__balance = __account_number,__account_holder,balance
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
    def withdraw(self,amount):
        if amount > self.__balance:
            print('Insufficient funds')
        else:
            self.__balance = self.__balance - amount
        return self.__balance
    def check_balance(self):
        return self.__balance

john = BankAccount("123456","John",1100.0)
john.deposit(1000.0)
john.withdraw(1500.0)
john.withdraw(600)
print(john.check_balance())


my_list = [1,2,3,4,5]
try:
    print(my_list[5])
except Exception:
    print("Exception")
except IndexError:
    print("IndexError")

#def error_function():
    #raise ValueError()
    #print("Print from error_function")
    #return "String from error_function"
#def print_without_error():
#    print("Print from print_without_error")
#try:
#    print_without_error()
#except ValueError:
#    print("We caught ValueError")
#else:
#    print("Print from else")
#    print(error_function())
#finally:
#    print("End of try...except")
#print("End of program")

try:
    print("Start program")
    result = function_sum(10,20)
    print("End program")
except Exception:
    print("We caught a bug")
finally:
    print("Finish")