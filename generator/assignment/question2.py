# Q2: Write a generator to yield squares of numbers from 1 to n.

def squares_upto(n):
    counting = 1
    while counting <= n:
        yield counting * counting
        counting += 1

for number in squares_upto(10):
    print(number)