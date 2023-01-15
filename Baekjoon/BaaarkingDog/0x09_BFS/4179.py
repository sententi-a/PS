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

row, col = map(int, sys.stdin.readline().split())

jihoon = deque()
fire = deque()
flag = False # 탈출 여부 
time = 0 # 탈출하는데 걸린 최소 시간 

maze = []

for i in range(col):
    maze.append(list(map(str, sys.stdin.readline().rstrip())))
    for j in range(row):
        if maze[i][j] == 'J':
            jihoon.append((i, j))
        if maze[i][j] == 'F':
            fire.append((i, j))


while jihoon:

    
    fire_x, fire_y = fire.popleft()

    for i in range(4):
        fire_nx, fire_ny = fire_x + dx[i], fire_y + dx[j]
        if 0 <= fire_nx < col and 0 <= fire_ny < row:
            if maze[fire_nx][fire_ny] == '.':
                maze[fire_nx][fire_ny] = 'F'
                fire.append((fire_nx, fire_ny))
                    