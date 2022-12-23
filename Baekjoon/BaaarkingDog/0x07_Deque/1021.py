# 회전하는 큐 https://www.acmicpc.net/problem/1021

"""
N개의 원소를 포함하고 있는 양방향 순환 큐
세 가지 연산을 수행할 수 있음
1. 첫 번째 원소를 뽑아냄
2. 왼쪽으로 한 칸 이동함
3. 오른쪽으로 한 칸 이동함 
"""

import sys
from collections import deque

deq_size, int_count = map(int, sys.stdin.readline().split()) # 큐의 크기, 뽑아내려고 하는 수의 개수 
targets = list(map(int, sys.stdin.readline().split())) # 뽑아내려고 하는 수의 위치
deq = deque([i for i in range(1, deq_size+1)])

operation_count = 0 # 2, 3번 연산의 개수 

for target in targets:
    while 1:
        if deq[0] == target:
            deq.popleft()
            break
        else:
            idx = deq.index(target)
            if idx < len(deq) / 2: # 만약, target이 위치하는 인덱스가 중간 앞이면 target을 만날 때까지 2번 연산
                while deq[0] != target:
                    deq.append(deq.popleft())
                    operation_count += 1
                
            else: # target이 위치하는 인덱스가 중간보다 뒤라면 target을 만날 때까지 3번 연산
                while deq[0] != target:
                    deq.appendleft(deq.pop())
                    operation_count += 1
              
print(operation_count)