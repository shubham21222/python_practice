#qus :- write program that  generates a sequence of numbers with a specified number of terms, where each term alternates between increasing by 2 and decreasing by 2, based on the initial value given by the user. The generated sequence is then printed.
value1 = int(input("enter the number(-1/1) : "))
n=int(input("enter number of terms: "))
list=[]
list.append(value1)
for i in range(n-1):
    if value1==-1:
        value1=value1+2
        list.append(value1)
    else:
        value1=value1-2
        list.append(value1)
print(list)
