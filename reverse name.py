"""
userstr=input("enter your string")
reverse=''
for i in range(len(userstr)-1,-1,-1):
    reverse=reverse+userstr[i]
print("user given string is {}", format(userstr))
print("reverse string is {}", format (reverse))


userstr=input("enter your string")
reverse=userstr[::-1]
print("user string =",userstr)
print("reverse=",reverse)
"""


'''list1=[15,12,13,14,15,16]
list1.append(23)
print(list1)
list1.remove(15)
print(id(list1))
print(list1)
print(id(list1))'''

l1=[15,12,14,13]
l2=[21,16,17]
print(l1,l2)
l1=l1+l2
print(l1)
# += polymorphism "one name different function"


l1=[15,12,14,13]
l2=[21,16,17]
print(l1,l2)
for i in l2:
    l1.append(i)
print(l1)

