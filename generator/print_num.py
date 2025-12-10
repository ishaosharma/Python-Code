def first(num):
    n = 1
    while n <= num:
        # yield n
        n = n + 1

values = first(100000000)
for x in values:
    print(x)



