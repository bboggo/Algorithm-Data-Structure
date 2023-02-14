import sys
n = list(sys.stdin.readline())
key = False

re = False
stack = []
reword= []
for word in n:
    if word == '<':
        key = True

    elif word == '>':
        stack.append('>')
        key = False

        print(reword)

    if key==True:
        stack.append(word)

print(stack)