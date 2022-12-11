name=input("enter string")
reverted=name[::-1]
if name==reverted:
    print("given string {} is palindrome" . format(name))
else:
    print("given string {} is not palindrome" . format(name))