# Demonstrate property with getter, setter, and deleter usage
#Here is a simple example demonstrating the use of `@property` with getter, setter, 
# and deleter in Python:

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        """Getter: Get the radius value"""
        print("Getting radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter: Set the radius value with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        print("Setting radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter: Delete the radius attribute"""
        print("Deleting radius")
        del self._radius


# Usage:
c = Circle(5)
print(c.radius)   # Calls getter, Output: Getting radius \n 5

c.radius = 10     # Calls setter, Output: Setting radius
print(c.radius)   # Output: Getting radius \n 10

del c.radius      # Calls deleter, Output: Deleting radius

# Further access would raise an AttributeError because _radius is deleted
# ### Explanation:
# - `@property` decorator marks the `radius` method as the getter, allowing you to access `c.radius` as if it's a regular attribute.
# - `@radius.setter` defines the setter for `radius` to validate and set its value.
# - `@radius.deleter` defines the deleter to delete the attribute when `del c.radius` is called.
# - This design encapsulates access to private `_radius` with controlled getting, setting, and deleting functionality.

# This approach provides elegant, safe attribute management with clean syntax that looks like standard attribute access but uses methods behind the scenes to enforce validation and behavior control.[1][4][5][6]
