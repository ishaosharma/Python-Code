#LIST METHODS
list = [2, 1, 3]
print(list)

list.append(4)  #adds one element at the end [2, 1, 3, 4]
print(list.append(5))  #returns None as appended 5 in the original list
print(list)             #list is mutable

list.sort()   #sorts in ascending order    [1,2,3,4]
print(list.sort())   #returns None and it only makes changes in the original list
print(list)

print(list.sort(reverse=True))  #descending order mein list sorted
print(list)

listing = ["banana" , "litchi", "apple"]
print(listing.sort())
print(listing)      #a<b<l
print(listing.sort(reverse=True))
print(listing)          #l>b>a in charater


grocery = ["kaju", "badam", "anaar", "aalo"]
grocery.reverse()               #reverses list
print(grocery)


#list.insert(index, element)   #insert element at index
numbers = [2, 5, 3]
print(numbers)
numbers.insert(1,4)
print("After inserting 4 at index 1 : ", numbers)

#list = [2,1,3,1] list.remove(1) ->removes first occurrence of element    [2,3,1]
number = [2,1,3,1]
number.remove(1)
print(number)

numbering = [3, 1, 4, 7]
numbering.pop(2)        #pop removes the element at index 2 which is 4 will be removed
print("After pop at index 2 the number 4 removed: ", numbering)  
