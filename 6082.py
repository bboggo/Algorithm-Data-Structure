a = input()
i=1
for j in range(1, int(a)+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=" ")
    else:
        print(i, end=" ")
    i += 1