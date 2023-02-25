import random
import statistics
randomlist1 = []
m = int(input("enter random values:  "))
for i in range(0,m):
    n = random.randint(1,30)
    randomlist1.append(n)
    print(randomlist1)
mean = sum(randomlist1)/len(randomlist1)
print(mean)
print("variance of list is :" , (statistics.variance(randomlist1)))
