#usecase 1: READING LARGE FILES

def read_large_file(file_path):
    """Generator to read large files line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

#Process 10GB file without loading it all in memory
for line in read_large_file('C:/Users/isha.sharma/Desktop/Python/generator/generator_use_case/gen.txt'):
    if 'error' in line:      #yielded line we have here
        print(f'Found error: {line}') 

