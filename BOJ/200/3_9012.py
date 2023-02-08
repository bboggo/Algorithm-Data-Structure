# 괄호
import sys

'''
1) 내 풀이
n = int(sys.stdin.readline())
for _ in range(n):
    text = sys.stdin.readline()
    ans = 0
    for a in text:
        if a =='(':
            ans += 1
        elif a == ')':
            ans -= 1
        if ans < 0:
            break
    if ans == 0:
        print("YES")
    else:
        print("NO")
'''

# 2) 스택으로 풀기
n = int(sys.stdin.readline())
for _ in range(n):
    text = sys.stdin.readline()
    stack = []
    for a in text:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')


