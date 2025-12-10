from functools import wraps
 
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function '{func.__name__}'called with arguments{args},{kwargs}")
        result=func(*args,**kwargs)
        print(f"Function'{func.__name__}'finished")
        return result
    return wrapper
 
@log_function_call
def greet(name):
    print(f"hello,{name}!")
 
@log_function_call
def add(a,b):
    return a+b
 
greet("isha")
print(add(4,3))