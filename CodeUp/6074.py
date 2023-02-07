text = input()
last = ord(text)
start = ord('a')
while start<=last:
    print(chr(start), end=' ')
    start+=1