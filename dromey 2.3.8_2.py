var1=1
n=int(input("enter number of terms: "))
list=[var1]
for i in range(1,n):
    var1 = var1 +2
    if i%2==0:
        list.append(var1)
    else:
        list.append(-(var1))

print(list)
print("sum of sequence : ",sum(list))