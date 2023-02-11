# 후위 표기식2
import sys

n = int(sys.stdin.readline())
sen = input()
num = [0] * n
ans = []

for i in range(n):
    num[i] = int(sys.stdin.readline())

for i in sen:
    if i.isalpha():
        ans.append(num[ord(i)-65])
    else:
        str2 = ans.pop()
        str1 = ans.pop()

        if i =='+':
            ans.append(float(str1) + float(str2))
        elif i == '-':
            ans.append(float(str1) - float(str2))
        elif i=='*':
            ans.append(float(str1) * float(str2))
        elif i=='/':
            ans.append(float(str1) / float(str2))
print('%.2f' %ans[0])

