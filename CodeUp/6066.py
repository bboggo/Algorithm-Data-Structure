a, b, c = input().split()
text = [int(a),int(b),int(c)]
for i in text:
    if i%2==0:
        print('even')
    else:
        print('odd')
