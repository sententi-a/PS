# 불! https://www.acmicpc.net/problem/4179

"""
미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해 지훈이가 불이 타기 전에 
탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지 결정해야 함

지훈이와 불은 매 분마다 한 칸씩 수평 또는 수직으로 이동
불은 각 지점에서 네 방향으로 확산
지훈이는 미로의 가장자리에 접한 공간에서 탈출 가능
지훈이와 불은 벽이 있는 공간은 통과하지 못함

#: 벽
.: 지나갈 수 있는 공간 
J: 지훈이의 미로에서의 초기 위치 (지나갈 수 있는 공간)
F: 불이 난 공간

불이 도달하기 전에 미로를 탈출할 수 없는 경우 IMPOSSIBLE
탈출할 수 있는 경우 가장 빠른 탈출 시간 출력
"""

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

col, row = map(int, sys.stdin.readline().split())

jihoon = deque()
fire = deque()
jh_visited = [[0 for _ in range(row)] for _ in range(col)]
fire_visited = [[0 for _ in range(row)] for _ in range(col)]

maze = []

for i in range(col):
    maze.append(list(map(str, sys.stdin.readline().rstrip())))
    for j in range(row):
        if maze[i][j] == 'J':
            jihoon.append((i, j))
        if maze[i][j] == 'F':
            fire.append((i, j))

# --------------- 불 이동 ---------------- #
while fire:

    x, y = fire.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < col and 0 <= ny < row:

            if not fire_visited[nx][ny] and maze[nx][ny] != '#':
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire.append((nx, ny))
            
# --------------- 지훈 이동 ---------------- #
while jihoon:

    x, y = jihoon.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < col and 0 <= ny < row:

            if not jh_visited[nx][ny] and maze[nx][ny] == '.':
                # 불이 아직 방문하지 않았거나 
                # 불이 퍼진 시간보다 지훈이가 이동한 시간이 더 빠르면, 이동할 수 있음
                if not fire_visited[nx][ny] or fire_visited[nx][ny] > jh_visited[x][y] + 1:
                    jh_visited[nx][ny] = jh_visited[x][y] + 1
                    jihoon.append((nx, ny))

        else:
            print(jh_visited[x][y] + 1)
            exit()


print("IMPOSSIBLE")
