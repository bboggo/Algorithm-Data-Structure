a, b, c = input().split()
day = 1
while(True):
    if day%int(a)==0 and day%int(b)==0 and day%int(c)==0:
        print(day)
        break
    day += 1