n = input()
for i in n:
    if i.islower():
        num = ord(i) + 13
        if num > 122:
            num -= 26
        print(chr(num), end="")
    elif i.isupper():
        num = ord(i) + 13
        if num > 90:
            num -= 26
        print(chr(num), end="")
    else:
        print(i,end="")