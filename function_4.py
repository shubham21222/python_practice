x=input("enter a value:")
def check(y):
    y=float(y)
    if int(y)/y==1:
       print("value is integer")
       return y
    elif y/int(y)>1:
        print("this is float")
        return y
    else:
        print("this is string")
        return y
check(x)