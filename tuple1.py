#qus:- simple tuple practice question
tuple1=(25,10,25.5,"star wars")
epic=tuple((25,10,11,0.75,"thor"))
print(epic,tuple1)
for i in tuple1:
    print("index=", tuple1.index(i))
    print("value=", i)
    print("type=", type(i)) #remove class (string)
    print("id=",id(i))
tuple1.pop("shubham")
print(tuple1)
