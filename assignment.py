#qus:- write a python program which take string as a input and change latters of string into uppercase latters.
input1 = input("Enter your string: ")
input2 = input("Enter another string with lowercase letters: ")


if len(input2) < len(input1):
    print("Error: The second string should be at least as long as the first string.")
else:
    result = ""

    for i in range(len(input1)):
        if input2[i] >= 'a' and input2[i] <= 'z':
            s = input1[i]
            s = ord(s)
            s = s - 32
            s = chr(s)
            result += s
        else:
            result += input1[i]

    print("Modified string:", result)
