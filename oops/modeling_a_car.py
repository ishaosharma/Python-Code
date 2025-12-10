class Car:
    def __init__(self,make_model,year):
        #instance varibles
        self.make_model = make_model
        self.year = year
        print("construction called")
    
    #instance method
    def start_engine(self):
        print("**Engine has started working**")
        print(f"Engine is of car model : {self.make_model}")
    def drive(self):
        print("**Driver is driving the car**")
        print(f"Driver is driving since {self.year} this model")

user = Car("Audi", 1990)
user.start_engine()
user.drive()


    