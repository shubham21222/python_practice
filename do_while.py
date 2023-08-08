#qus:- write a calculator program that performs arithmetic operations on two numbers using do while loop.
def calculator():
	print("Welcome to My Calculator")
	var1 = int(input("Enter Value1 : "))
	var2 = int(input("Enter Value2 : "))
	oper_choice = input("Please in Operation of your choice :\n1 for Addition \n2 for Substraction \n3 for Multiplication \n4 for Division\n Please Enter Your Choice :  ")
	if oper_choice == "1" : 
		result = var1 + var2
		print(result) 
	elif oper_choice == "2":
		result = var1 - var2
		print(result)
	elif oper_choice == "3":
		result = var1 * var2 
		print(result)
	elif oper_choice == "4":
		result = var1/var2
		print(result)
	else : 
		print("invalid operation given")
		calculator()

def check():
	num_char=["0","1","2","3","4","5","6","7","8","9"]

	num_count = 0
	dot_count = 0
	other_count = 0
	for i in result:
		if i in num_char:
			num_count += 1
		elif i == ".":
			dot_count += 1
		else:
			other_count +=1
	if other_count == 0 and dot_count ==0:
		result = int(result)

	elif other_count == 0 and dot_count ==1:
		result = float(result)
	else:
		result = str(result)
	return result
result = check()

print('result = '  ,result)
print(type(result))

def next_move():
	next_choice = input("Enter y to continue or n to close : ")
	if next_choice == "y":
		return True
	elif next_choice == "n":
		return False
	else : 
		print("Invalid Input")
		next_move()

while True : 
	calculator()
	var3 = next_move()
	if var3 == True :
		calculator()

	elif var3 == False: 
		print("Thanks for using my calculator")
		break

