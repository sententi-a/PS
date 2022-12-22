# 덱 https://www.acmicpc.net/problem/10866

import sys
from collections import deque

deq = deque()

for _ in range(int(sys.stdin.readline())):
    case = list(sys.stdin.readline().split())

    if case[0] == "push_front":
        deq.appendleft(int(case[1]))
    elif case[0] == "push_back":
        deq.append(int(case[1]))
    elif case[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif case[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif case[0] == "size":
        print(len(deq))
    elif case[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif case[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif case[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)