# Q4: Create a generator that yields lines from a text file one by one.

#To create a generator that yields lines from a text file one by one, you can write a simple generator function like this:

def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
          #  print(line)         # At this point, file is automatically closed
            yield line.strip()  # yield each line without trailing whitespace
    
for line in read_lines('C:/Users/isha.sharma/Desktop/Python/generator/assignment/example.txt'):
    print(line)         #The for loop then iterates over each yielded line, printing it.






### Explanation in simple words:

# - The function `read_lines` takes a filename as input.
# - It opens the file in read mode (`'r'`).
# - It loops over the file line by line.
# - Instead of returning all lines at once, it uses `yield` to return one line at a time.
# - Each yielded line is stripped of unnecessary spaces or newline characters at the end.
# - This way, you can read large files efficiently without loading the whole file in memory.

### How to use it:
# for line in read_lines('example.txt'):
#     print(line)


#This loop will print each line in the file one by one, using the generator.

### Why use this:
# - It’s memory-efficient, especially for huge files.
# - You process one line at a time, so your program stays responsive and uses less RAM.
# This simple generator function is a common, practical pattern for handling large text files line-by-line [based on common Python usage].