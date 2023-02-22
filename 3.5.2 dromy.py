list1 = []
n = int(input("enter number of prime factors: "))
m = int(input("enter last number of prime factors: "))
for i in range (n,m+1):
    if i%2!=0 and i!=2:
        list1.append(i)
    #print(list1)
    if  i!=3 and  i%3!=0 and i%2!=0  :
        list1.append(i)
    if i%5!=0 and i%3!=0 and i%2!=0 and i!=5:
        list1.append(i)
    if i%7==0 and i%2!=0 and i%3!=0 and i%5!=0  and i!=3 and i!=5:
        list1.append(i)
print(list1)