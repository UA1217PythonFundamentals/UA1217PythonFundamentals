class Employee():
  '''Test class for task #10_1_3'''
  counter = 0

  def __init__(self,name,salary):
    Employee.counter += 1
    self.name = name
    self.salary = salary

  def info(self):
    return f'Employee {self.name} has a salary of {self.salary}$'
  
  @classmethod
  def total_number(cls):
    return f'Total number of employees: {cls.counter}'
  

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)


devops = Employee("Stas Tarasenko", 5000)
sre = Employee("Some Guy", 6000)

print(devops.info())
print(Employee.total_number())