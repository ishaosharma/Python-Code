light = "pink"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("go slow")
else:
    print("Light is broken")
print("end of code")


age = 97

if(age>=18):
    print("can vote")  #indentation
else:
    print("cannot vote")



#nesting
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#qns
number = int(input("Enter any number : "))
if(number % 2 == 0):
    print("Number is even")
else:
    print("Number is Odd")

#qns
num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
num3 = int(input("Enter number3 : "))

if(num1 >= num2 and num1 >= num3):
    print("num1 is greater number among 3 numbers entered by user ", num1)
elif(num2 >= num3):
    print("num2 is greater than num1 and num3 ", num2)
else:
    print("num3 is greater number among 3 numbers entered by user ", num3)


#qns
numberof7 = int(input("Enter number to check multiple of 7 or not: "))
if(numberof7 % 7 == 0):
    print("Number is multiple of 7 : ",numberof7)
else:
    print("Not a multiple of 7: ", numberof7)






#qns
marks = float(input("Enter your marks : ")) 

if(marks>=90):
   grade = "A"
elif(marks>=80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
   grade = "C"
else:
    grade = "D"

print("Grade of the student is - ", grade)






