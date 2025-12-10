#=Chaining generators involves nesting generator calls so one generator consumes the output of another.
#=Chains can be deep and complex but remain readable and maintainable.
#=The yield from syntax (introduced in Python 3.3) simplifies delegation to sub-generators, 
# improving clarity in chaining.

def generator_a():
    yield from range(3)

def generator_b():
    yield from generator_a()
    yield from range(3, 6)

for value in generator_b():
    print(value)



# Pipelining and chaining enable modular, composable data processing workflows.

# They allow working with large or infinite data streams efficiently, minimizing memory use.

# These patterns fit well in real-time data processing, web scraping, simulations, and more.

# In summary, pipelining and chaining with generators create elegant, 
# memory-efficient sequences of operations where each generator handles one step, 
# passing its output downstream. This is an advanced and powerful pattern for handling iterative processing 
# in Python
