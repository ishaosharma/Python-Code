class MathHelper:
    @staticmethod
    def add_numbers(x, y):
        return x + y

# You can call it with the class, no object needed:
result = MathHelper.add_numbers(2, 3)
print(result)  # Output: 5


# Explained Simply:
# @staticmethod is a built-in decorator.
# The method add_numbers does not use self (it doesn’t need any info about instances of the class).
# You can call MathHelper.add_numbers(2, 3) directly without creating any object.
# Static methods are useful for utility functions related to a class but not needing instance data.