# 그림 https://www.acmicpc.net/problem/1926

"""
큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이 출력하기
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림
그림의 넓이란 그림에 포함된 1의 개수
"""

import sys
from collections import deque

paper = []
queue = deque()
count = 0 # 그림 개수
max_area = 0 # 그림의 최대 넓이

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

height, width = map(int, sys.stdin.readline().split()) # 도화지 세로, 가로 크기
#visited = [[False for _ in range(width)] for _ in range(height)]

for _ in range(height):
    paper.append(list(map(int, sys.stdin.readline().split())))

def bfs(nx, ny):
    global max_area
    temp = 1
    queue.append((nx, ny))
    paper[nx][ny] = 0
    #visited[nx][ny] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]
            if 0 <= mx <height and 0<= my < width:
                #if not visited[mx][my]:
                if paper[mx][my] == 1:
                    temp += 1
                    queue.append((mx, my))
                    #visited[mx][my] = True
                    paper[mx][my] = 0

    max_area = max(max_area, temp)

for i in range(height):
    for j in range(width):
        if paper[i][j] == 1:
            count += 1
            bfs(i, j)

print(count, max_area, sep="\n")