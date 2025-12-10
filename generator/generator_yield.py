def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D' #Now this generator is responsible to generate 4 values

g = mygen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#now if asked for 5th time so gives error of : StopIteration
print(next(g))