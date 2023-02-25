import random
import math
r1 = random.random()
print("r1 =",r1)
r2 = random.random()
print("r2 =",r2)
d = (2*r1-1)**2+(2*r2-1)**2
print(d)

if d >= 1 :
    n1 = ((-2*math.log10(d))/(d))**(1/2)
    n_1 = n1*(2*r1-1)
    print("n_1 =",n_1)
    n2 = (-2*math.log10(d))
    n_2 = (n2/d)**(1/2)
    n__2 = (n_2)*(2*r2-1)
    print("n__2 =",n__2)

