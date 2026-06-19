#simple calcualor project
print("simple calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")


choice=int(input("enter your choice:"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))

if choice==1:
    result=num1+num2
    print("Answer=",result)
elif choice==2:
    result=num1-num2
    print("Answer=",result)
elif choice==3:
    result=num1*num2
    print("Answer=",result)
elif choice==4:
    if num2 !=0:
        result=num1/num2
        print("Answer=",result)
    else:
        print("cannot divide by zero")
else:
    print("invalid choice")
