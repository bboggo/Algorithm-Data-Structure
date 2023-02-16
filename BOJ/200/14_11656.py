n = input()
stack = []
for i in n:
    stack.append(n)
    n = n[1:]
for _ in sorted(stack):
    print(_)
