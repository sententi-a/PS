# 트리의 부모 찾기 https://www.acmicpc.net/problem/11725

import sys 
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline()) # 노드의 개수 
graph = [[0 for i in range(n+1)]for i in range(n+1)] # 각 인덱스별 부모 노드 
visited = [False for i in range(n+1)] # 방문 체크
parent = [0 for i in range(n+1)] # 각 인덱스 별 부모 노드의 키를 담은 리스트

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v: int):
    visited[v] = True
    for i in range(1, n+1):
        if graph[v][i] != 0 and not visited[i]:
            parent[i] = v # 부모 노드를 직접 연결되어 있는 노드로 정해줌 
            dfs(i)

dfs(1)
print(*parent[2:], sep="\n")