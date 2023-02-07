d=[]
for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    d[i] = list(map(int, input().split()))

print(d)