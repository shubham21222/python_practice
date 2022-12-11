print("Enter String: ", end="")
text = input()

for i in range(len(text)):
    if text[i]>='a' and text[i]<='z':
        ch = text[i]
        ch = ord(ch)
        ch = ch-32
        ch = chr(ch)
        text = text[:i] + ch + text[i+1:]

print("\nIts Uppercase:", text)