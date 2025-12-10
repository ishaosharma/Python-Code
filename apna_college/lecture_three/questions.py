# movies = []
# print("Enter the names of your 3 favorite movies")
# movies.append(input("Enter movie1 : "))
# movie2 = input("Enter movie2 : ")
# movies.append(movie2)
# movie3 = input("Enter movie3 : ")
# movies.append(movie3)

# print(movies)
# print(type(movies)) 


#PALINDROME means aage and peeche se same to same like 1,2,1 and maam
list= ["M", "A", "A", "M"]
# list= [1, 2, 3, 2, 1]
# list= [1, 2, 3]
copied_list = list.copy()   #list ki copy banai
copied_list.reverse()       #then reverse kardia 

if(list == copied_list):
    print("List is palindrome")
else:
    print("List is not palindrome")


grades = ("C","D","A", "A","B","B","A" )  
print("Number of students who scored grade A are: ",grades.count("A"))

grading = ["C","D","A", "A","B","B","A"] 
print(grading)
grading.sort()
print("After sorting: ", grading) 