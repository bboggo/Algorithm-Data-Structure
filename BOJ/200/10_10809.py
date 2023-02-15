n = input()
alp = [-1] * 26
for i in range(len(n)):
    if alp[ord(n[i])-97] == -1:
        alp[ord(n[i])-97] = i

print(*alp)