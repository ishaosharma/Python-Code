class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2 

c = Circle(5)
print(c.area)  # Output: 78.5 (accessed like attribute, not method)



