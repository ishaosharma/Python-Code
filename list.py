my_list = [1,2,3]
print(my_list)

my_listt = [1,'Aarvi',5]
print(my_listt)


my_listing = list((1,2,8))
print(my_listing)



my_listings = list(range(5))
print(my_listings)

final_list = list(range(5,21,5))
print(final_list)


#conversion of string into list
name = "aman"
l1 = list(name)
print(l1)

#Dynamically provided value how we can get list
# values = []
# values = eval(input("Enter list : "))
# print(values)
# print(type(values))


valuess = "Python Django FastAPI Flask"
list_val = valuess.split()
print(list_val)
print(type(list_val))


items = [0,1,2,3,4,5,6,7,8,9,10]
print(items)
items[3] = 77
print(items)

iteming = [0, 1,2, list("python")]
print(iteming) 

itemss = [10,20,[30,40]]
print(itemss)
print(itemss[2])
print(itemss[2][0])
print(itemss[2][1]) 

# LIST COMPREHENSION

items_list = []
for val in range(1,11):
    items_list.append(val*val)
print("items list is : ",items_list)

#using list comprehension we can write above code in one line
itemm_list = [item*item for item in range(1,20)]
print("using comprehension : ", itemm_list)


final_list1 = [x*x for x in range(1,11)]
final_list2 = [x+x for x in range(1,11)]
print(final_list1)
print(final_list2)

#in the list we want to select only even no.s
data_list = [1,2,3,4,5,6,77,44,56,77]
even_list = [val for val in data_list if val%2 == 0]
print(even_list)

# The below code uses a list comprehension to create a new list of numbers based on a specific condition.
# itemsing = [x**2 for x in range(1,11) if (x**2)%2 != 0]
# range(1, 11) generates numbers from 1 to 10.
# For each number x in this range, x**2 calculates its square (x*x).
# if (x**2)%2 != 0 includes only those squares that are odd (not divisible by 2).
# The resulting list contains the odd squares between 1 and 10.

itemsing = [x**2 for x in range(1,11) if (x**2)%2 != 0]
print(itemsing) 


words = ["Hello","class","good","morning"]
fianl_listt = [word for word in words if len(word) > 5]
print(fianl_listt) 


#which number present in n1 but not in n2
n1 = [10,20,30,40]
n2 =[30,40,50,60]
n3 = [x for x in n1 if x not in n2]
print(n3)

#Traversing elements in list and accessing elements
list1 = [10,20,30,40]
index = 0
while index < len(list1):
    print("List1 is : ",list1[index])
    index = index + 1

#using for loop doing traversal in list
list2 = [100,204,330,420,550]
for item in list2:
    print(item)

#using for loop print even no.s in list
items_lisst = [0,1,2,3,4,5,6,7,8,9]
for item in items_lisst:
    if item % 2 == 0:
        print(item) 


# {} acts like a slot or placeholder in the string.
# When you use .format(value), the value is inserted where {} is placed.
# You can have multiple {} in a string and pass multiple values to .format().
# Optionally, you can put numbers or names inside {} to specify which argument to use or to reorder them.
# Curly braces are part of Python's "replacement fields" for dynamic string creation.
items1 = [10, 20, 30, 40, 50]
index = 0
length = len(items1)  # avoid using 'len' as variable name because it's a built-in function

for item in items1:
    print("{} is available at +ve index {} and at -ve index {}".format(item, index, index - length))
    index += 1 
 
#example of .format(name, age)
name = "Aman"
age = 25
print("My name is {} and I am {} years old".format(name, age))



# The key part to understand is the end=" " parameter in the print() function:
# By default, print() ends with a newline character (\n), so every print outputs on a new line.
# Here, end=" " changes that behavior so that after each printed value, a space is printed instead of a new line.
# This makes all the numbers appear on the same line separated by spaces.
# In simple words: The end=" " part tells print() to print a space after each number instead of moving to a new line, so all numbers print side by side with spaces in between.

# data_list = [1,2,3,4,5,6,77,44,56,77]
# for val in data_list: 
#     print(val,end =" ")


#qns
items3 = [0,1,1,1,3,2,2,1,4,4,6,7,8]
value = 12
if items3.count(value) > 0 :
    print(items3.index(value)) 
print("Value not present") 


