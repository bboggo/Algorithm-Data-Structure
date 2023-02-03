a, b, c = input().split()
(print(a) if int(a)<int(c) else print(c))if int(a)<int(b) else (print(c) if int(c)<int(b) else print(b))