# 스택 https://www.acmicpc.net/problem/10828

"""
스택을 구현한 후, 입력을 주어지는 명령 처리하기
push X 
pop
size
empty
top 
"""

import sys

stack = []
answers = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == "push":
        stack.append(int(command[1]))

    elif command[0] == "pop":
        if stack:
            answers.append(stack.pop())
        else:
            answers.append(-1)

    elif command[0] == "size":
        answers.append(len(stack))

    elif command[0] == "empty":
        if stack:
            answers.append(0)
        else:
            answers.append(1)

    elif command[0] == "top":
        if stack:
            answers.append(stack[-1])
        else:
            answers.append(-1)

print(*answers, sep="\n")
