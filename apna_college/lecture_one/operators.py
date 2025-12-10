#arithmetic operators
# a=5
# b=2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)   #result of division in python is aways in float. 4/2 = 2 but in python it will be 2.0 only
# print(a%b)   #remainder
# print(a**b)  #a^b a to the power b -- 5^2 = 5*5= 25

#Relational/comparison operators
a = 50 
b = 20
print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

#Assignment operators (==, +=,-=,*=,/=,%=,**=)
num = 10
# num += 5
num %= 5
print("num : ", num) 

#logical operators(not, and, or)
a = 50
b = 20
print(not True)
print(not False)
print(not (a>b))

val1 = True
val2 = True
print("and operator: ", val1 and val2) 
print("OR operator: ", val1 or val2)  

val3 = True
val4 = False 
print("and1 operator: ", val3 and val4) 
print("OR1 operator: ", val3 or val4) 

#Type Conversion
a = float("2")
b = 4.25

print(type(a))
print(a + b)

pi = 3.14
pi = str(pi)

print(type(pi))
