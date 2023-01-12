n = int(input("Enter the number of numbers you want to sum: "))
total = 0
list = []
for i in range(n):
    number = int(input("Enter number {}: ".format(i + 1)))
    total += number
    list.append(number)

print("The sum of {} numbers is: {}".format(n, total))
print(list)