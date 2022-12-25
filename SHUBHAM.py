operation = input("select the operation : (+,-,*,/)")
X=[".0"]

num1=float(input("enter the first number :"))

num2 = float(input("enter the second number :"))

if operation== "+" :
    print(num1+num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1*num2)

elif operation == "/":
    a=num1/num2
    if a==a(X):
        print(int(a))
    else :
        print(float(a))
else:
    print("invalid operation")