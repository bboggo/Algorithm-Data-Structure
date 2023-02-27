import sys

n = int(sys.stdin.readline())
for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    a, b = A, B
    while b!= 0:
        a = a % b
        a, b = b, a
    print(A * B // a)