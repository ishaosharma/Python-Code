print("Isha")

#multiplication
print(10*3)

#repetition
print("hello" * 5)
print(5 * "hello")

#exponent
print(10**2)

#chaining of relational operator
print(10<20<30) #T 
print(10<20>30<40)  #F
print(10==5+5==20-10==5*2)  #T 


prime_member=["amit", "sachin","rajesh","suresh","mukesh","naina"]
member="amit"
if member in prime_member:
    print("You are a prime member")
else:
    print("You are not a prime member")


prime_member=["amit", "sachin","rajesh","suresh","mukesh","naina"]
member="nehal"
if member not in prime_member:
    print("You are not a prime member")
else:
    print("You are a prime member")



num1=10
num2=20
num3=10
print(num1 is num2)  #F 
print(num1 is num3)  #T
print(num1 is not num2) #T  BOTH ARE POINTING DFFRNT
print(num1 is not num3) #F  Both are pointing same


#2 ways pof declaring strings using '' and ""
str1 = 'dsdhcb'
print(str1)
print(type(str1))

str2 = "niudwd"
print(type(str2))

#multiline string
str3 = """hubsdb"""
print(type(str3))

str = "hello class"
#del - delete the object form memory

print(str)
# del str 

str = str.replace("hello", "")
print(str)


#1st assignment 
tech_string = "Python Programming Practice"
print(tech_string)

print(tech_string[0])
print(tech_string[-1])
print(tech_string[13])
print(tech_string[0:4])
print(tech_string[1:5])



b = "Hello World!"
print(b[-5:-2])  #orl

test_string = "Python string negative indexing practice for developers"
#negative_indexing_exercises
print(test_string[-30:-3])
print(test_string[-1])
print(test_string[-2])
print(test_string[-3])
print(test_string[-4:-1])


tech = "python" 
print(tech)
print(tech[2:5]) 
print(tech[:]) 
print(tech[::2]) #it will skip 1 character after every character 

print(tech[::1])   #Left TO Right  as +ve index of step  
#reverse the string
print(tech[::-1])  #nohtyp  R to L as -ve index 

