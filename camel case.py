#take a variable and alocate a user define string in it.
#now take another variable and alocate  and value to it.
#repeat the below step for 9 times
#take ith index character if i(!=1):
#  
value1=input("enter the string")
value2=''
for i in range (len(value1)):
    if i !=1:
        value2=value2+value1[i].lower()
    else:
        value2=value2+value1[i].upper()
    print("user given value=",value1)
    print("camel case of given value=",value2)           
    