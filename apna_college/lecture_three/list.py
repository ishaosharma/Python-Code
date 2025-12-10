#Lists in Python
#A built-in data type that stores set of values
#It can store elements of different types(integer, float, string, etc..)
#List is MUTABLE in python

marks = [94.4, 89.5, 95.2, 66.4, 45.1]
print(marks)
print(len(marks))   #returns length of list
print(marks[0])
print(marks[1])

student = ["Karan", 85, 17, "Delhi"]
print(student)
print(student[0])
print(len(student))
student[0] = "arjun"
print(student)



#LIST SLICING: returns sublist of list
#list_name[starting_index : ending_index]    -> ending index is not included

markss = [78, 57, 98, 93, 82, 74]
print(markss[1:4])
print(markss[:4])  #by default starts from 0 index
print(markss[:])    #by default starts from 0 index and goes till last index
print(markss[1:])   #by default last index is the ending index


#negative indexing
print(markss[-3:-1])   #-3 se -1 tak jaaiga and -1 is not included