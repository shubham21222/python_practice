#qus:- write a python program to which takes a list and gives number of passed students and failed students. 
marks = [23, 50, 53, 54, 62, 21]
passing_marks = 50
total = sum(marks)
print("Total marks:", total)

passed_students = []
failed_students = []

for i in marks:
    if i >= passing_marks:
        passed_students.append(i)
    else:
        failed_students.append(i)

print("Passed students:", passed_students)
print("Failed students:", failed_students)
