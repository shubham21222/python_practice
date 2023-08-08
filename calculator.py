#qus:- write a python program for construct a calculator which is taking arithmatic operation with user.


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input("enter your choice:1/2/3/4 " ))
if choice in ('1','2','3','4'):

 num1=float(input("enter first number"))
 num2=float(input("enter second number "))

 if choice=='1':
    add=num1+num2
    print("addition of number is:",add)

 elif choice=='2':
    subtract=num1-num2
    print("subtraction of numbers is:", subtract)

 elif choice=='3':
    multipication=num1*num2
    print("multipication of numbers is",multipication)

 elif choice=='4':
    divide=num1/num2
    print("division of number is:", divide)

else:
    print("invalid input")