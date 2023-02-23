'''n = int(input("enter a number : "))
list1= []
sum=0
for i in range(1,n+1):
    if n%i==0 :
        list1.append(i) 
print (list1)

for i in list1:
    if i==n:
        break
    else:
        sum=sum+i


if sum == n :
    print("number is a perfact number")
else :
    print("enter number is a not a perfact number")'''



per = []

def perfact(n):
    list1=[]
    global sum
    sum=0

    for i in range(1,n+1):
        if n%i==0 :
            list1.append(i) 

    for i in list1:
        if i==n:
            break
        else:
            sum=sum+i


    if sum == n :
        per.append(sum)

for i in range(1,10000):
    perfact(i)
print(per)
    

