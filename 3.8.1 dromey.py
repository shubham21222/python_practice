def fab(n):
    if n == 1 or n == 0:
        return n
    return fab(n-1) + fab(n-2)
n = 10
for i in range(0,n):
    print(fab(i))