# 트리의 부모 찾기 https://www.acmicpc.net/problem/11725

import sys 
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline()) # 노드의 개수 
graph = [[]for i in range(n+1)] # 각 인덱스별 부모 노드 
parent = [0 for i in range(n+1)] # 방문 체크(0 or 양의정수) + 각 인덱스 별 부모 노드 저장

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v: int):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v # 부모 노드를 직접 연결되어 있는 노드로 정해줌 
            dfs(i)

dfs(1)
print(*parent[2:], sep="\n")