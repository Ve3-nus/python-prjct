from abc import ABC, abstractmethod

# (Abstraction)
class Employee(ABC):
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self._salary = salary  # Encapsulation - salary is kept private

    @abstractmethod
    def calculate_bonus(self):
        pass

    def get_details(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: {self._salary}"
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, annual_leave):
        super().__init__(name, emp_id, salary)
        self.annual_leave = annual_leave

    # Polymorphism: Overriding calculate_bonus method
    def calculate_bonus(self):
        return self._salary * 0.10  # 10% bonus

# Subclass for PartTimeEmployee - Inheritance
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, hours_worked):
        super().__init__(name, emp_id, salary)
        self.hours_worked = hours_worked

    # Polymorphism: Overriding calculate_bonus method
    def calculate_bonus(self):
        return self.hours_worked * 10  # $10 bonus per hour worked

# Department Class to manage employees in each department
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self):
        return [emp.get_details() for emp in self.employees]