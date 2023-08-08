#qus :- write a basic calculto program which is perform operations with two variables.

def calc():
    print("welcome to my calculator")
    var1 = float(input("Enter Value1 : "))
    var2 = float(input("Enter Value2 : "))
    oper_choice = input("Please in Operation of your choice :\n1 for Addition \n2 for Substraction \n3 for Multiplication \n4 for Division \n5 for power \n Please Enter Your Choice :  ")
    if   oper_choice == "1" : 
        result = var1 + var2
        print(result) 
    elif oper_choice == "2":
        result = var1 - var2
        print(result)
    elif oper_choice == "3":
        result = var1 * var2 
        print(result)
    elif oper_choice == "4":
        result = var1 / var2
        #except ZeroDivisionError:
        print(result)
    elif oper_choice =="5":
        result = var1 ** var2 
        print(result)
    else: 
        print("invalid operation given")
        calc()   