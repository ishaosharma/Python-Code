class Sample:
    def __init__(self, name):
        self.name = name
 
    @property
    def print_name(self):
        return self.name
   
obj = Sample("Ankur")
print(obj.print_name)

#print_name is a method but by using the built-in decoratr we can call it as a attribute or object
#as you can see we have not parenthesis after print_name. 