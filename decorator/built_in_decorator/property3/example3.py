class Student:
    def __init__(self, emp_name):
        self.emp_name = emp_name

    @property
    def print_name(self):
        return self.emp_name

naming = Student("Isha")
print(naming.print_name)
