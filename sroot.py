'''x=40
y=1/2
squareroot=x**y
print(squareroot)'''

#import time as t
from time import *
x=int(input("enter no:"))
start_time= time()
y=1
for i in range (1,x+1):
  y=y*i 
print("fractional of {} is {}" . format (x,y))

end_time= time()
total=end_time-start_time
print(total)