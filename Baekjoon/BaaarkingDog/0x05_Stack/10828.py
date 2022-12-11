# 스택 https://www.acmicpc.net/problem/10828

################# 	30616KB	48ms ##########################

"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys 

stack = []

for _ in range(int(sys.stdin.readline())):

    case = list(sys.stdin.readline().split())

    if case[0] == "push":
        stack.append(int(case[1]))
        
    elif case[0] == "pop":
        if len(stack) == 0:
            print(-1)     
        else:
            print(stack.pop())

    elif case[0] == "size":
        print(len(stack))

    elif case[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])