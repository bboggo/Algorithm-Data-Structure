import sys

n, k = int(sys.stdin.readline())
queue = []
l = [] * n
for i in range(n):
    l[i] = i
for i in range(n):
    