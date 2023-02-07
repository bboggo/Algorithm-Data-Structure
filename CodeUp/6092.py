n = int(input())
a = input().split()
d= []
for j in range(24):
    d.append(0)

for i in range(0, int(n)):
    num = int(a[i])
    d[num] += 1

for k in range(1, 24):
    print(d[k], end=' ')