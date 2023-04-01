list1 = [28,26,25,11,16,12,24,29,6,10]

i = 0
j = len(list1)-1

k= 17

while i<j:
    if list1[i]<k:
        i = i+1
    elif list1[j]>k:
        j= j-1
    else:
        list1[i],list1[j]=list1[j],list1[i]
        i = i+1
        j = j-1

print("array is : ",list1)
