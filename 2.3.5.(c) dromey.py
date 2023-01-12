n=int(input("enter no. of terms : "))
list=[]
var1=2
list.append(var1)
for i in range(1,n,1):
        var1 = var1+2
        list.append(var1)
        total=sum(list)
        continue 
print(list)
print("sum of all numbers: ",total)
