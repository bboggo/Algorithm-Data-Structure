import sys
n = input()
alp = [0] * 26
for i in n:
    alp[ord(i)-97] += 1

print(*alp)