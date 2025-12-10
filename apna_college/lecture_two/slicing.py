#slicing  - Accesing parts of string (Substring)   
#str[start_index: ending_index]    and ending index is not included
str = "apna college"

#positive indexing
print(str[0:5])
print(str[5:12])
print(str[:4]) # is same as [0:4]
print(str[5:]) #[5:len(str)]
print(str)
print(str[5:len(str)])

#Negative indexing
strr = "Apple"
print(strr[-3:-1])  #-3 se -1 tak print hoga and -1 is not included in it so pl is o/p
print(strr[-5:-2])   #app as o/p