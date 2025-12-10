# Q1: Create a generator that yields even numbers up to n.
 
def even_no_up_to(n):
    counting = 1
    while counting < n:
        if counting % 2 == 0:
            yield counting
        counting += 1

for number in even_no_up_to(5):
    print(number) 