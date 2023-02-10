# 오큰수
import sys
'''
1) 내 코드 - 타임 오버

ans = []
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
test = 0

for i in range(len(num)):
    FK = True
    for j in range(i+1, len(num)):
        if num[i]<num[j]:
            ans.append(num[j])
            FK = True
            test += 1
            break
        else:
            FK = False

    if FK == False:
        ans.append('-1')
        test += 1

    if i == len(num)-1:
        ans.append('-1')
        test += 1

print(*ans)

'''

# 2) 스택을 이용한 풀이

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
stack = []
stack.append(0)
answer = [-1] * n
for i in range(1, n):
    while stack and num[stack[-1]] < num[i]:
        answer[stack.pop()] = num[i]
    stack.append(i)

print(*answer)