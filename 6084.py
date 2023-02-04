a, b, c, d = input().split()
print(format(int(a)*int(b)*int(c)*int(d)/8/1024/1024, '.1f') + ' MB')