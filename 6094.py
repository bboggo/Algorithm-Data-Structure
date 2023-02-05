n = int(input())
a = input().split()
num = 20
for i in range(0, int(n)):
    if int(num) < int(a[i]):
        num = num
    elif int(num) > int(a[i]):
        num = int(a[i])
print(num)