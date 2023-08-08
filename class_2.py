#qus:- write a python program which take stdent name and marks as a input and short it and gives student result as output.
class Student:
    def getMarks(self):
        number_of_students = int(input("please enter the number of students : "))
        students = []
        while number_of_students!=0:
            name = input("please enter the name :")
            mark = input("please enter the mark :")
            x = [name,mark]
            students.append(x)
            number_of_students -= 1
        return students

    def getDict(self):
        dict = {}
        for item in self.getMarks():
            dict[item[0]] = item[1]
        return dict

    def getIntendMark(self):
    dict = self.getDict()
    place = 0
    n = 0 # if you had 1 student it was giving out of bound error
    sort = sorted([x for x in dict.values()])
    if len(sort)>1:  # I check the list length 
        n=1
    print(len(sort))
    for item in sort:
        if sort[0] == sort[n]:
            if n < len(sort):
                n += 1
        else:
            place = n

    mark = sort[place]
    return (mark, dict.items())

    def showAnswer(self):
        nomre,dict = self.getIntendMark()
        #dict = self.getDict().items() #you are calling getMarks() 2nd times

        for key,value in dict:
            if value == nomre:
                return f"answer:: name is {key} , mark is {nomre}"


if __name__ == "__main__":
    s = Student()
    # print(s.getMarks())
    # print(s.getDict())
    # print(s.sortMarks())
    # print(s.getIntendMark())
    print(s.showAnswer())