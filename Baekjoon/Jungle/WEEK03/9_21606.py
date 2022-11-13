# 아침산책 acmicpc.net/21606

import sys 
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
info = [0] + list(map(int, sys.stdin.readline().strip())) # 장소 정보 (실내: 1, 실외: 0)
tree = [[] for i in range(n+1)]
count_inside = 0

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a) 
    if info[a] == info[b] == 1:
        count_inside += 2

def dfs(v: int, count_outside):
    visited[v] = True
    for node in tree[v]: 
        if info[node] == 1: # 인접한 곳이 실내면 + 1
                count_outside += 1
        elif info[node] == 0 and not visited[node]: # 인접한 곳이 실외면 또 탐색
                count_outside = dfs(node, count_outside)
    return count_outside

visited = [False for i in range(n+1)]
sum_of_outside = 0

for i in range(1, n+1): 
    if not visited[i] and info[i] == 0:
        x = dfs(i, 0)
        sum_of_outside +=x * (x-1)

print(sum_of_outside + count_inside)