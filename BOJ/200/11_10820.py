while(True):
    try:
        n = input()
        small, big, num, nul = 0, 0, 0, 0
        for i in n:
            if i.isupper():
                big += 1
            elif i.islower():
                small += 1
            elif i == ' ':
                nul += 1
            else:
                num += 1
        print(small, big, num, nul)
    except EOFError:
        break