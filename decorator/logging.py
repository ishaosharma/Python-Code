#3- Logging

@log_calls
def add(x,y):
    return x + y
add(2,3)

#OUTPUT:
# INFO:root: Calling add with args(2,3) and kwargs {}
# INFO:root:Function add returned 5 

