class Employee:
    number_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1

    @classmethod
    def numb_of_employees(cls):
        print(f"Total number of employees: {cls.number_of_employees}")

    def info(self):
        print(f"Name{self.name}, Salary: {self.salary}")


emp1 = Employee("Alex", 3000)
emp2 = Employee("Adel", 5000)


emp1.info()
emp2.info()
Employee.numb_of_employees()

print(f"Base classes: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")