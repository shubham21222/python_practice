input1=input("enter your string")
x=len(input1)
shubham = input()
for i in range (x):
    if shubham[i]>='a' and shubham[i]<='z':
        s = x[i]
        s = ord(s)
        s = s-32
        s = chr(s)
        x = x[::1] + s + x[i+1:] 
print ("uppercase :" , x)        
