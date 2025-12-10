#Solution1 : Memory-Efficient Large Sequences

#With Generator

def large_sequence_generator(n):
    for i in range(n):
        yield i*2

#only one value in memory at a time
gen = large_sequence_generator(1000000)
for item in gen:
    if item > 100:
        break #Rest of values never computed!
