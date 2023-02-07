a = input()
i=0
total = 0
for j in range(1, int(a)+2):
    if i%2==0:
        total += i
    i += 1
print(total)