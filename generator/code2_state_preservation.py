#State preservation is a core feature of Pythin Generators.
#Example of state preservation:

def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

#create a generator object
counter = count_up_to(3)
print("counter : ",counter)

#First call: Execution starts
print(next(counter))  #o/p = 1

#second call : Execution resumes from where it left off
print(next(counter))  #o/p = 2

#Third call: Execution resumes again
print(next(counter))  #o/p = 3

#Fourth call : The generator is exhausted
print(next(counter))   #Raise StopIteration
