def avg(*y):
    sum=0
    for i in y:
     sum=sum+i
    average=sum/len(y)
    return average

value1=avg(2,4,6,7)
value2=avg(4,5,8,2,11,23)
value3=avg(21001,212,314,35)

print(value1)
print(value2)
print(value3)   