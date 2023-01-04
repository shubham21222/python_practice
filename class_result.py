def getStudentDetails():
    
        students = []
        global number_of_students 
        while number_of_students!=0:
            name = input("Enter Name : ")
            physics =int(input("Enter Physics Marks : "))
            chemistry = int(input("Enter Chemistry Marks : "))
            maths = int(input("Enter Math Marks : "))  
            x = [name,physics,chemistry,maths]
            students.append(x)
            number_of_students -= 1
            
         
        return students 

number_of_students = int(input("please enter the number of students : "))
      
# S1=Student()
s = getStudentDetails()

print(s)

marks = open("class_marks.txt","w")
marks1= type(str(marks))
marks.write(marks1)
marks.close()

#Step 2 : reading marks from marks1.txt and calculating average and total marks  
data_file = open("class_marks.txt","r")
data = data_file.read()
#print(data)
record = data.split(",")
#print(record)
total = 0 
for i in range(1,len(record)):
    total = total + int(record[i])
average = total/(len(record)-1)
print(total,average)
data_file.close()