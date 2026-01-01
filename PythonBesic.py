print("Welcome to python")
print("Lets create a calculator")
first=input("Enter the first number:")
sec=input("Enter the second number:")
print("Mini projecgt using python:")
first=int(first)
sec=int(sec)
i=1
while(1):
    print("....Menue....")
    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")
    print("5.%")
    print("6.Exit")
    op=input("Enter your option:")
    op=int(op)
    if op==1:
        print("The result=",first+sec)
    elif op==2:
        print("The result=",first-sec)
    elif op==3:
        print("The result=",first*sec)
    elif op==4:
        print("The result=",first/sec)
    elif op==5:
        print("The result=",first%sec)
    elif op==6:
        break
    else:
        print("Invalid operation")

'''
x="Tondra Rahman"
print("The value of x=",x.upper())
print("The value of x=",x.lower())
print("find function=",'R' in x)
if(3>3):
    print("Hello world")
else:
    print("nothing")
arr=range(6)
j=1
for j in arr:
 print(j)
print("Use of while loop:")
i=9
while(i<81):
    print(i)
    i*=2

print("list data type in python:")
marks=[99,95,97]
print(marks)
print("the third list element:",marks[2])
print("Adding new elementts in list:")
marks.append(45)
print(marks)
print("Checking existance elemant in list:")
print(45 in marks)
print("Length of list:")
print(len(marks))
print("WHile loop to print list:")
i=0
while(i<len(marks)):
   print(marks[i])
   i+=1
print("Tuple concepts:")
marks=(99,95,96,97,100)
print(marks)
print("Sets in pythons:")
marks={99,95,97,99,100}
print(marks)
print("Python is finished")

'''
