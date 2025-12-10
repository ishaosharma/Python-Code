class Employee:
    def __init__(self,emp_name):
        self.emp_name = emp_name

    @property
    def print_employee_name(self):
        return self.emp_name

name = Employee("Isha")
print(name.print_employee_name) 
