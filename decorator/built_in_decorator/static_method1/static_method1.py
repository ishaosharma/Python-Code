# @staticmethod
# Defines a method inside a class that doesn't require instance or object (self) or class (cls) reference.
# Acts like a regular function but lives in the class namespace.
#for static/class variable we use @staticmetod

class Math:
    @staticmethod
    def add(x, y):
        return x + y

# You can call it with the class, no object needed:
print(Math.add(5, 3))  # Output: 8 



# @staticmethod is a built-in decorator.
# The method add does not use self (it doesn’t need any info about instances of the class).
# You can call Math.add(2, 3) directly without creating any object.
# Static methods are useful for utility functions related to a class but not needing instance data.


