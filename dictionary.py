dict1={"name":"shubham","class":"bca","subject":"maths",}
dict2={1:"23",2:"25",3:"26",3:"27"}
print(dict1)
for i in dict1:
    print(i) #print keys
    print(dict1[i]) 
for i,j in dict2.items(): #odered
    print(i)
    print(j)    

dict1["name"]="shub"
print(dict1)
dict1["school"]="svm"
print(dict1)
dict1.pop("name")
print(dict1)