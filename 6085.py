r,g,b = input().split()
print(format(int(r)*int(b)*int(g)/8/1024/1024, '.2f') + ' MB')