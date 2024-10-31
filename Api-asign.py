from abc import ABC, abstractmethod

# (Abstraction)
class Employee(ABC):
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self._salary = salary 

    def get_details(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: {self._salary}"
    

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, annual_leave):
        super().__init__(name, emp_id, salary)
        self.annual_leave = annual_leave

    # Polymorphism
    def calculate_bonus(self):
        return self._salary * 0.11

#  Inheritance
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, hours_worked):
        super().__init__(name, emp_id, salary)
        self.hours_worked = hours_worked

    # Polymorphism: 
    def calculate_bonus(self):
        return self.hours_worked * 10 

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
        return [emp.get_details() for emp in self.employees]# Main program to interact with the Employee Management System
def main():
    # Create Department
    hr_department = Department("Human Resources")

          #Add Full-Time Employee
    emp1 = FullTimeEmployee("Alice", "F123", 60000, 25)
    hr_department.add_employee(emp1)

      # Add Part-Time Employee
    emp2 = PartTimeEmployee("Bob", "P456", 20000, 150)
    hr_department.add_employee(emp2)

       # Display All Employees
    print("Employees in HR Department:")
    for emp_details in hr_department.list_employees():
        print(emp_details)

    # Show Bonus ==polymorphism
    print("\nBonus Calculations:")
    for emp in hr_department.employees:
        print(f"{emp.name}'s Bonus: ${emp.calculate_bonus()}")

    # Remove an Employee
    hr_department.remove_employee("F123")
    print("\nUpdated Employees in HR Department after removal:")
    for emp_details in hr_department.list_employees():
        print(emp_details)

# Run the main function
if __name__ == "__main__":
    main()
