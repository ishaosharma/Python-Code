#problems we faced before generators

#problem1 : memory issues with large lists
def create_large_list(n):
    result = []
    for i in range(n):
        result.append(i*2)
    return result

#This creates a list with 1 million elements in memory!
large_list = create_large_list(1000000)
for item in large_list:
    if item > 100:      #we only need first few items
        break