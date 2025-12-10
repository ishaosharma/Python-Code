#Strings - String is data type that stores a sequence of characters.
#String is IMMUTABLE in Python

name='this is string'
name1="this is string and we mostly use this declaration of string in python"
name2="""this is also string"""
name3='''this is string'''

print(name)
print(name1)
print(name2)
print(name3)

#escape sequence character : \n - new line, \t - tab space
str = "Hello \nI am isha"
print(str)
str1 = "Hello \tI am isha"
print(str1) 

#Basic operation of string
#1. Concatenation
word1 = "Hello"
word2 = "Ram"
final_word = word1 + " " + word2
print(final_word) 

#2. Length of str
print(len(word1))
print(len(final_word)) 
