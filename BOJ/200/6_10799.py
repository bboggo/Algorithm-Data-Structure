import sys
n = list(sys.stdin.readline())
ans = 0
stack = []
for i in range(len(n)-1):
    if n[i] == '(':
        stack.append('(')
    else:
        if n[i-1] == '(':
            stack.pop()
            ans += len(stack)

        else:
            stack.pop()
            ans += 1

print(ans)

