import sys

n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
ans = 0
for i in numbers:
    num = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                num += 1
        if num == 0:
            ans += 1
print(ans)