class employee:
    def __init__(self):
        self.name = input("enter name: ")
        self.emloyeeid = input("enter employee ID : ")
        self.contact = input("enter contact no. : ")
        self.address = input("enter address: ")
        self.dept = input("enter department : ")

    def show_detil(self):
        print("emplyee name : ", self.name)
        print("employee ID : ", self.emloyeeid)
        print("adresss:", self.address)
        print("contact:", self.contact)
        print("department", self.dept)

    def dwrite(self):
        f = open("employee.txt", "a")
        data = self.emloyeeid+" ,"+self.name+"," + \
            self.address+","+self.contact+","+self.dept+"\n"
        f.write(data)
        print("data entered sucessfully")


class manager(employee):
    #employee(). __init__()

    def dept_employee_detail(self):
        f = open("employee.txt")
        data = f.read()
        data_row = data.split("\n")
        data_row.pop()
        valid_row = []
        for i in data_row:
            x = i.split(",")
            if self.dept == x[len(x)-1]:
                valid_row.append(i)


'''emp = manager()
emp.show_detil()
emp.dwrite()'''


class owner (manager, employee):
    def show_all(self):
        f = open("employee.txt", "r")
        data = f.read()
        data_row = data.split("\n")
        data_row.pop()
        for i in data_row:
            x = i.split(",")
            print("-----------------")
            print("employee ID ", x[0])
            print("employee name", x[1])
            print("employee contact", x[2])
            print("address", x[3])
            print("department", x[4])
        print("------------------")


s1 = employee()
s2 = manager()
s3 = owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()
s1.show_detil()
s2.show_detil()
s2.dept_employee_detail()
s3.show_detil()
s3.dept_employee_detail()
s3.show_detil()

emp = manager()
emp.show_detil()
emp.dwrite()
