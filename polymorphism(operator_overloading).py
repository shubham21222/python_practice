class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("part A",self.a)
        print("part B",self.b)
    def __add__ (self,other):
        x= self.a+other.a
        y=self.b+other.b
        z = test(x,y)
        return z

s1=test(42,27)
s2=test(27,42)
s3 = s1+s2
s3.show()

'''a = 3
b = 2
c= a . __add__(b)
print(c)'''