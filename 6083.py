a, b, c = input().split()
total = 0
for i in range(0, int(a)):
    for j in range(0, int(b)):
        for k in range(0, int(c)):
            print(i, j, k)
            total += 1
print(total)
