tuple = (2, 1, 3, 1)   #and  tuple = (2, 1, 3, 1,)  also valid way to declare tuple 
print(tuple)
print(type(tuple))
print(tuple[0])
print(tuple[1])
print(tuple[2]) 

#tuple[0] = 5 #error as tuples are immutable


#Empty tuple
tup = ()
print(tup)
print(type(tup))


#Single value tuple mein , lagaaana is essential so that python take it as class tuple only 
single_tup = (1,)
print(single_tup)
print(type(single_tup))

tupp = (1)
print(type(tupp))
tupp = ("shree")
print(type(tupp))

tupp_str = ("shreeleela",)
print(type(tupp_str)) #bcoz , we have specified so it will consider class tuple only and not string class

#TUPLE SLICING
numbers = (1,4, 6, 8)
print(numbers[1:3])  #index 3 not included
print(numbers[-4:-1])  #index -4 se index -1 tak jaiga and -1 index ka value not included

