# DFS와 BFS https://www.acmicpc.net/problem/1260

import sys 
from collections import deque

n, m, v = map(int,sys.stdin.readline().split()) # 정점 개수, 간선 개수, 탐색 시작할 정점의 번호 (1~N)

graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # 그래프를 나타낼 2차원 배열
visited_bfs = [False for _ in range(n+1)] # 방문 체크 _ bfs
visited_dfs = [False for _ in range(n+1)] # 방문 체크 _ dfs


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v: int):
    """먼저 방문할 정점을 매개변수로 전달하면 그곳부터 시작해 너비 우선 탐색을 하며 방문한 정점을 print"""
    visited_bfs[v] = 1 
    queue = deque()
    queue.append(v)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(1, n+1):
            if graph[node][i] != 0 and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                

def dfs_recursion(v: int):
    """먼저 방문할 정점을 매개변수로 전달하면 그곳부터 시작해 깊이 우선 탐색을 하며 방문한 정점을 print"""
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(n+1):
        if graph[v][i] !=0 and not visited_dfs[i]:
            dfs_recursion(i)

def dfs_stack(v:int):
    visited_dfs[v] = 1
    stack = deque()
    stack.append(v)

    while stack:
        node = stack.pop()
        print(node, end=" ")
        for i in range(1, n+1):
            if graph[node][i] != 0 and not visited_dfs[i]:
                dfs_stack(i)
    return
    
dfs_stack(v)
print()
bfs(v)

