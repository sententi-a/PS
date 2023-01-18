# 유기농 배추 https://acmicpc.net/problem/1012

"""
어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있음
그래서 그 배추들 역시 해충으로부터 보호받을 수 있음

서로 인접해있는 배추들이 몇 군데에 퍼져 있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있음
"""

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(sys.stdin.readline())):
    row, col, num = map(int, sys.stdin.readline().split()) # 배추밭 가로 길이, 세로 길이, 배추 개수
    baechu = [[0 for _ in range(row)] for _ in range(col)]
    
    queue = deque()
    start = []
    count = 0 # 배추흰지렁이 최소 개수

    for _ in range(num):
        y, x = map(int, sys.stdin.readline().split())
        baechu[x][y] = 1
        start.append((x, y)) # 배추가 심어진 곳
        # queue.append((x, y))

    for a, b in start:

        if baechu[a][b] == 1:  # 배추가 심어져있고, 다른 배추들과 인접하지 않은 곳이라면 count
            count += 1
            queue.append((a, b)) 

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < col and 0 <= ny < row:
                        if baechu[nx][ny] == 1:
                            queue.append((nx, ny))
                            baechu[nx][ny] = 0
    
    print(count)