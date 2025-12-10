str = "io am a coder in python"

print(str.endswith("er"))   #Returns true if string ends with substr er
print(str.capitalize()) #Capitalize 1st character and makes a new string and no changes in original string
#if you want the change to reflect in original string as well then str = str.capitalize() now it will chnage in original string only

# str.replace(old,new)    -> replaces all occurences of old-python with new-pythan 
print(str.replace("python", "pythan")) 

#str.find(word)           -> returns 1st index of 1st occurences
print(str.find("o"))
print(str.find("coder"))
print(str.find("Q"))   # returns -1 

#str.count("am")  counts the occurences of substring
print(str.count("coder"))
print(str.count("o"))