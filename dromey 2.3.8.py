value1= 1
value2= -3
n=int(input("enter number of terms: "))
list=[]
list.append(value1)
list.append(value2)
for i in range(1,n):
    if value1==1:
        value1=value1+4
    list.append(value1)
    if value2==-3:
      value2=value2+(-4)
    list.append(value2)     
print(list)