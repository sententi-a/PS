# 이분 그래프 https://www.acmicpc.net/problem/1707

import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline()) # 테스트 케이스 개수


def dfs(v: int, color:int):
    global is_bipartite_graph

    if not is_bipartite_graph:
        return

    visited[v] = color
    for node in graph[v]:
        if not visited[node]: 
            dfs(node, -color)

        elif visited[node] == visited[v]: # 인접한 곳인데 색이 같다면
            is_bipartite_graph = False
            return

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 개수 
    graph = [[] for i in range(v+1)] # 빈 그래프
    visited = [False for i in range(v+1)] # 방문 체크
    is_bipartite_graph = True

    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v+1):
        if not visited[i]:
            dfs(i, 1)
            if not is_bipartite_graph:
                break

    print('YES' if is_bipartite_graph else 'NO', end="\n")



