w, h = input().split()
n = input()
d=[]
for i in range(int(w)):
    d.append([])
    for j in range(int(h)):
        d[i].append(0)
for i in range(int(n)):
    l, t, x, y = input().split()
    if t == '0':
        for j in range(int(l)):
            d[int(x)-1][int(y)-1+j] = 1
    elif t == '1':
        for j in range(int(l)):
            d[int(x)-1+j][int(y)-1] = 1

for i in range(int(w)):
    for j in range(int(h)):
        print(d[i][j], end=' ')
    print()
