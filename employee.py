#implementation of Employee class
class Employee:
    def __init__(self, name:str, age:int, position:str, salary:float):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'Employee(Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary:.2f})'

    def update_position(self, new_position):
        self.position = new_position

    def update_salary(self, new_salary):
        self.salary = new_salary

# Implementation of company class

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                return True
        return False

    def update_employee(self, name, new_position=None, new_salary=None):
        for emp in self.employees:
            if emp.name == name:
                if new_position:
                    emp.update_position(new_position)
                if new_salary:
                    emp.update_salary(new_salary)
                return True
        return False

    def view_all_employees(self):
        for emp in self.employees:
            print(emp)

    def find_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

# Employee user interface
def main():
    company = Company()
    
    while True:
        print("\nCompany Employee Management System")
        print("1. Add a new employee")
        print("2. Remove an employee")
        print("3. Update an employee's details")
        print("4. View all employees")
        print("5. Find an employee by name")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter employee's name: ")
            age = int(input("Enter employee's age: "))
            position = input("Enter employee's position: ")
            salary = float(input("Enter employee's salary: "))
            new_employee = Employee(name, age, position, salary)
            company.add_employee(new_employee)
            print(f'Employee {name} added successfully.')

        elif choice == '2':
            name = input("Enter the name of the employee to remove: ")
            if company.remove_employee(name):
                print(f'Employee {name} removed successfully.')
            else:
                print(f'Employee {name} not found.')

        elif choice == '3':
            name = input("Enter the name of the employee to update: ")
            emp = company.find_employee(name)
            if emp:
                print(f'Current details: {emp}')
                new_position = input("Enter new position (leave blank to skip): ")
                new_salary = input("Enter new salary (leave blank to skip): ")
                if new_position == '':
                    new_position = None
                if new_salary == '':
                    new_salary = None
                else:
                    new_salary = float(new_salary)
                if company.update_employee(name, new_position, new_salary):
                    print(f'Employee {name} updated successfully.')
                else:
                    print(f'Failed to update employee {name}.')
            else:
                print(f'Employee {name} not found.')

        elif choice == '4':
            company.view_all_employees()

        elif choice == '5':
            name = input("Enter the name of the employee to find: ")
            emp = company.find_employee(name)
            if emp:
                print(emp)
            else:
                print(f'Employee {name} not found.')

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

