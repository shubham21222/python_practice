# this code demonstrates how to implement a "do-while" loop in Python using functions.

def dowhile(func = None, condition = None):
    if not func or not condition:
        return
    else:
        func()
        while condition():
            func()
x = 10
def f():
    global x
    x = x - 1
def c():
    global x
    return x > 0
dowhile(f, c)
print (x)
