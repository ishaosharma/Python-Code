# In Python, pipelining and chaining with generators refer to the practice of 
# linking multiple generator functions together so that the output of one generator 
# becomes the input to the next, creating a streamlined sequence of data processing steps. 
# This technique mimics the pipeline pattern found in software engineering, where 
# data flows through several stages, each performing a specific transformation.

# Generator Pipelining:
#-Pipelining means performing a series of operations sequentially on each element of an iterable, 
# with the output of one stage feeding into the input of the next.

#-Each stage in the pipeline is implemented as a generator that yields 
# processed elements one by one.

#-This setup allows lazy evaluation throughout the chain, conserving memory and 
# improving efficiency by processing items only as needed.

def integers():
    for i in range(1, 6):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

def negated(seq):
    for i in seq:
        yield -i

pipeline = negated(squared(integers()))

for value in pipeline:
    print(value)

# Here, integers() yields numbers from 1 to 5, squared() squares each incoming number, and negated() negates each squared number. 
# The pipeline chains these steps seamlessly.


