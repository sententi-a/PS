# 큐 https://www.acmicpc.net/problem/10845

import sys 
from collections import deque

q = deque()

for _ in range(int(sys.stdin.readline())):
    case = list(sys.stdin.readline().split())

    if case[0] == 'push':
        q.append(int(case[1]))
    elif case[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif case[0] == 'size':
        print(len(q))
    elif case[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif case[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif case[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)