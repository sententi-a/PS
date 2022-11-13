# 아침산책 acmicpc.net/21606

import sys 
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
info = [0] + list(map(int, sys.stdin.readline().strip())) # 장소 정보 (실내: 1, 실외: 0)
tree = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

count = 0

def dfs(v: int):
    global count
    visited[v] = True
    # stack.append(v) # 디버깅용 

    for node in tree[v]: # 만약 실외면 인접 노드를 계속 탐색, 실내면 경로가 끝나므로 count += 1
        if not visited[node]: 
            if info[node] == 0:
                dfs(node)
            else:
                count += 1
    
for i in range(1, n+1):
    visited = [False for i in range(n+1)]
    # stack = [] # 디버깅용 
    if info[i] == 1:
        dfs(i)
    # print(stack) # 디버깅용 

print(count)