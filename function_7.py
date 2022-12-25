def checktype(x):
    num_chr=["0","1","2","3","4","5","6","7","8","9"]

    num_count=0
    dot_count=0
    other_count=0
    for i in x:
        if i in num_chr:
            num_count+=1
        elif i==".":
            dot_count+=1
        else:
            other_count+=1
        
    if other_count==0 and dot_count==0:
       x=int(x)
        
    elif other_count==0 and dot_count==1:
       x=float(x)
        
    else:
        x=str(x)
        return x
y=input("enter value:")
y=checktype(y)

print("user value=", y)

print("user value type=",type(y))