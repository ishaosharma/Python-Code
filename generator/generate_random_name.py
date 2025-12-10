from random import *
def namegen():
    num = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        name = ''
        for i in range(6):
            name += choice(num)
        yield name
for i in namegen():
    print(i)



# Explanation in simple words:
# namegen is a generator function that produces random uppercase 6-letter strings endlessly.

# Inside namegen:
# It endlessly runs an infinite loop.
# For each iteration, it creates an empty string name.
# Then, in a loop of length 6, it picks a random letter from the alphabet using choice(num) and adds it to name.
# After making a 6-letter string, it yields (returns) this name.
# The for loop outside calls namegen() and prints each generated random name.
# This will print a continuous stream of random 6-letter uppercase names, one per line.

# Key concepts:
# choice(num) picks one character randomly from the uppercase alphabet.
# yield produces a value that you can iterate over, generating one name at a time.
# The infinite while True loop means it never stops generating new names unless interrupted.
# This is an efficient way to generate random data on demand without storing all names in memory.