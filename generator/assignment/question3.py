# Q3: Write a generator that yields Fibonacci numbers up to n terms.

def fibonacci_gene(n):
    a, b = 0, 1
    for _ in range(n):    # _ means repeat/run this block 5 times but (don't use the loop variable) i dont care about the actual no. (0,1,2,3,4)
        yield a
        a, b = b, a+b
 
for i in fibonacci_gene(7):
    print(i) 


# DRY RUN: 
# a , b = b , a+b
# a = 0, b = 1
# a = 1, b = 1
# a = 1, b  = 2
# a = 2, b = 1+2 = 3
# a = 3, b = 2+3 = 5



