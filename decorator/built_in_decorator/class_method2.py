# @classmethod
# Defines a method that takes the class itself as the first argument (cls).
# Used to access or modify class state, or create alternative constructors.
# for class method decorator we use @classmethod built-in decorator

class Employee:
    raise_amount = 1.05

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount 

Employee.set_raise_amount(1.1)
print(Employee.raise_amount)  # Output: 1.1
