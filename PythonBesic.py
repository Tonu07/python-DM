print("Welcome to python")
print("Lets create a calculator")
first=input("Enter the first number:")
sec=input("Enter the second number:")
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
