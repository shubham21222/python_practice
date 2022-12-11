divisor=int(input("enter a number"))
x= list(range(1,divisor+1))
divisorlist=[]
for number in x:
    if divisor % number == 0:
      divisorlist.append(number)
    print(divisorlist)
