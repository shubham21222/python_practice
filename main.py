#import sample1
# import sample1 as s
from sample1 import *
#calculating permutation:-
n,r =int(input("enter value: ")),int(input("enter value of r:"))
'''if r<=n:
    result= s.factorial(n)/s.factorial(n-r)
    print(result)
else :
    print("please take n greater than r")'''

if r<=n:
    result= factorial(n)/factorial(r)*factorial(n-r)
print(result)