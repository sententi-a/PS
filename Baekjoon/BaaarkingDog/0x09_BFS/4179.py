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

count = 0 # 지훈이가 한 타임에 위치할 수 있는 좌표의 개수
jihoon = deque()
fire = deque()
time = 0 # 탈출하는데 걸린 최소 시간 

maze = []

for i in range(col):
    maze.append(list(map(str, sys.stdin.readline().rstrip())))
    for j in range(row):
        if maze[i][j] == 'J':
            jihoon.append((i, j))
            count += 1
        if maze[i][j] == 'F':
            fire.append((i, j))


while jihoon:
    
    time += 1

    # --------------- 지훈 이동 ---------------- #
    jh_x, jh_y = jihoon.popleft()
    maze[jh_x][jh_y] = '.'
    count -= 1
    
    for i in range(4):
        jh_nx, jh_ny = jh_x + dx[i], jh_y + dy[i]

        if 0 <= jh_nx < col and 0 <= jh_ny < row:
            if maze[jh_nx][jh_ny] == '.':
                # 지훈이가 미로의 가장자리에 접한 공간에 도달하면 탈출 
                if jh_nx == 0 or jh_nx == col - 1 or jh_ny == 0 or jh_ny == row - 1:
                    print(time)
                    exit()
                maze[jh_nx][jh_ny] = 'J'
                count += 1
                jihoon.append((jh_nx, jh_ny))


    # --------------- 불 이동 ---------------- #
    if fire:
        fire_x, fire_y = fire.popleft()

        for i in range(4):
            fire_nx, fire_ny = fire_x + dx[i], fire_y + dy[i]
            if 0 <= fire_nx < col and 0 <= fire_ny < row:
        
                # 불이 옮겨 붙을 위치
                if maze[fire_nx][fire_ny] == '.' or maze[fire_nx][fire_ny] == 'J':
                    maze[fire_nx][fire_ny] = 'F'
                    fire.append((fire_nx, fire_ny))
                    # 그 중 지훈이가 위치할 수 있는 곳이라면... 
                    if maze[fire_nx][fire_ny] == 'J':
                        count -= 1

                # 지훈이가 불에 휩싸였다면  
                if count <= 0:
                    print("IMPOSSIBLE")
                    exit()
                
    
    # for l in maze:
    #     print(*l)
