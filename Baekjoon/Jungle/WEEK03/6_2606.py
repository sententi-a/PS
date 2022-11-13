# 바이러스 https://www.acmicpc.net/problem/2606
# 나와 직접 연결되지 않았지만 간접적으로 연결된 컴퓨터까지 모두 봐야하므로 dfs를 사용해야 함

import sys
from collections import deque

n = int(sys.stdin.readline()) # 컴퓨터의 수 (정점의 수)
m = int(sys.stdin.readline()) # 컴퓨터 쌍의 수 (간선의 수) 

computers = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answers = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    computers[a][b] = computers[b][a] = 1

def dfs(v: int):
    visited[v] = 1
    for i in range(1, n+1):
        if computers[v][i] != 0 and not visited[i]:
            answers.append(i)
            dfs(i)

dfs(1)
print(len(answers))
