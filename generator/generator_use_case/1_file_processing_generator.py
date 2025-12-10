#1-File Processing Generator
#Create a generator that reads a file and yields lines that contain a specific keyword.


def read_lines(filename):
    keyword = "Jin chan"
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                yield line

for line in read_lines('C:/Users/isha.sharma/Desktop/Python/generator/generator_use_case/exam.txt'):
    print(line)   