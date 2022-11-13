# 연결 요소의 개수 https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = 1

visited = [False for _ in range(n+1)]

def dfs(v: int):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] != 0:
            dfs(i)
    
count = 0

for i in range(1, n+1):
    if visited[i]: continue
    dfs(i)
    count += 1 # dfs를 몇 번 돌렸는지 카운트 == 연결 요소의 개수
print(count)  
