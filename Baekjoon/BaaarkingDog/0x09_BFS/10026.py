# 적록색약 https://acmicpc.net/problem/10026

"""
적록색약 R, G 구분 어려움 
그림이 주어졌을 때, 적록색약인 사람이 봤을 때와 
아닌 사람이 봤을 때 구역의 수를 구하는 프로그램 작성
"""

import sys
from collections import deque

queue_n = deque([(0, 0)])
queue_b = deque([[0, 0]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

grid = [] # 그림

col = int(sys.stdin.readline())
for _ in range(col):
    grid.append(list(map(str, sys.stdin.readline().rstrip())))
row = len(grid[0])

visited_n = [[0 for _ in range(row)] for _ in range(col)]
visited_b = [[0 for _ in range(row)] for _ in range(col)]

count_n = 0
count_b = 0


for i in range(col):
    for j in range(row):
        # 적록색약이 아닌 사람이 봤을 때의 구역 구하기
        if visited_n[i][j] == 0:
            queue_n.append((i, j))
            # print(i, j)
            count_n += 1
            while queue_n:
                x, y = queue_n.popleft()
                color = grid[x][y]

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < col and 0 <= ny < row:
                        if visited_n[nx][ny] == 0 and grid[nx][ny] == color:
                            queue_n.append((nx, ny))
                            visited_n[nx][ny] = 1
        # 적록색약인 사람이 봤을 때의 구역 구하기 
        if visited_b[i][j] == 0:
            queue_b.append((i, j))
            count_b += 1
            while queue_b:
                x, y = queue_b.popleft()
                color = grid[x][y]

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < col and 0 <= ny < row:
                        if visited_b[nx][ny] == 0:
                            if color == 'R' or color == 'G':
                                if grid[nx][ny] == 'R' or grid[nx][ny] == 'G':
                                    queue_b.append((nx, ny))
                                    visited_b[nx][ny] = 1
                            else:
                                if grid[nx][ny] == color:
                                    queue_b.append((nx, ny))
                                    visited_b[nx][ny] = 1

print(count_n, count_b)