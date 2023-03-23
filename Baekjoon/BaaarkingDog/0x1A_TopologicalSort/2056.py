# 작업 https://www.acmicpc.net/problem/2056

import sys
from collections import deque
from heapq import heappush, heappop

n = int(sys.stdin.readline())
answer = 0
queue = deque()

# 작업은 우선순위 큐에 넣을까

graph = [[] for _ in range(n+1)]
times = [0 for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for i in range(n):
    _input = tuple(map(int, sys.stdin.readline().split()))
    times[i+1] = _input[0] 
    indegree[i+1] += _input[1]
    
    for j in range(_input[1]):
        graph[_input[j+2]].append(i+1)
    
queue.append((1, times[1]))
# answer += times[1]

while queue :
    task, task_time = queue.popleft()
    answer += task_time

    temp = []
    for adj in graph[task]:
        print(adj, indegree[adj])
        if indegree[adj] > 0:
            indegree[adj] -= 1
        
        if indegree[adj] == 0:
            temp.append((adj, times[adj]))
            # queue.append(adj)
            # answer += times[adj]
    if temp:
        temp.sort(key=lambda x: x[1])
        print(temp)
        queue.extend(temp)

print(answer)