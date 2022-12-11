x=input("enter your string")
i=len(x)
for j in range (len(x)):
    if x[i]>='a' and x[i]<='z':
      s=x[i]
      s=ord(s)
      s=s-32
      s=chr(s)
print("its uppercase", x)

