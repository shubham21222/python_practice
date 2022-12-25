def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x* fact(x-1)
var1=int(input("enter value:"))
result=fact(var1)
print("factorial of {}={}". format(var1,result))