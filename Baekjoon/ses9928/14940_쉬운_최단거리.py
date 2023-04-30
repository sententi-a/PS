# 쉬운 최단거리 https://www.acmicpc.net/problem/14940

"""
모든 지점에 대해 목표지점까지의 거리 구하기
가로, 세로로만 움직일 수 있음
"""

import sys 
from collections import deque

row, col = map(int, sys.stdin.readline().split())

graph = []
dists = [[0 for _ in range(col)] for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
queue = deque()

for i in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))

    for j in range(col):
        if graph[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = True
            target = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < row and 0 <= ny < col:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                dists[nx][ny] = dists[x][y] + 1

# 출력
for i in range(row):
    for j in range(col):
        # 원래 갈 수 있는 땅 중 도달할 수 없는 위치는 -1 출력 
        if dists[i][j] == 0 and (i != target[0] or j != target[1]) and graph[i][j] == 1:
            print(-1, end=" ")
            continue

        print(dists[i][j], end=" ")
    print()