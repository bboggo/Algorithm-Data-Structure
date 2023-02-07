# 단어 뒤집기
import sys
'''
1) reverse 메소드 이용
n = int(sys.stdin.readline())
for i in range(n):
    text = sys.stdin.readline().split()
    for j in text:
        answer = list(j)
        answer.reverse()
        for k in range(len(answer)):
            print(answer[k], end="")
        print('', end=" ")
    print('')
'''
# 2) 스택을 이용
n = int(sys.stdin.readline())
for i in range(n):
    text = sys.stdin.readline().split()
    reverse_text = []

    for word in text:
        reverse_text.append(word[::-1])
    answer = " ".join(reverse_text)
    print(answer)