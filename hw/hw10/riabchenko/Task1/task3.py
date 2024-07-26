class Employee:
    """Task 3"""
    

    employee_count = 0


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1


    def display_employee_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")


    def display_class_info(self):
        print(f"Class name: {self.__class__.__name__}")
        print(f"Module name: {self.__class__.__module__}")
        print(f"Base classes:")
        for base in self.__class__.__bases__:
            print(f"  - {base.__name__}")
        print(f"Class namespace:")
        for key, value in self.__class__.__dict__.items():
            print(f"  - {key}: {value}")
        print(f"Documentation: {self.__class__.__doc__}")


def collect_employee_data():
    employees = []
    while True:
        name = input("Enter employee name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        salary = float(input("Enter employee salary: "))
        employees.append(Employee(name, salary))
    return employees


employees = collect_employee_data()


for employee in employees:
    print(employee.display_employee_info())


Employee.print_total_employees()


print("\nClass information for each employee:")
for employee in employees:
    print("\nClass information for", employee.name)
    employee.display_class_info()
