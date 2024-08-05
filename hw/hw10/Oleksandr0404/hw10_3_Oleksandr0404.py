class Employee:
    # Class attribute to keep track of the number of employees
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1  # Increment employee count whenever a new employee is created

    def display_employee_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def display_total_employees(cls):
        return f"Total number of employees: {cls.employee_count}"

# Example usage
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

# Display information about the class
print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

# Display information about employees
print(employee1.display_employee_info())  # Output: Name: Alice, Salary: 50000
print(employee2.display_employee_info())  # Output: Name: Bob, Salary: 60000

# Display total number of employees
print(Employee.display_total_employees())  # Output: Total number of employees: 2
