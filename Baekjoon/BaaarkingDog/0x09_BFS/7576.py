# 토마토 https://www.acmicpc.net/problem/7576

"""
정수 1은 익은 토마토,
정수 0은 익지 않은 토마토, 
정수 -1은 토마토가 들어있지 않은 칸
토마토가 모두 익을 때까지의 걸리는 일수의 최솟값 출력
모든 토마토가 익어있다면 0, 모두 익지는 못하는 상황이면 -1 
"""

import sys
from collections import deque

hor, ver = map(int, sys.stdin.readline().split())

days = 0
tomato = [] # 토마토 정보 담은 리스트
rotten = [] # 초기에 익은 토마토 좌표 저장하는 리스트
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(ver):
    tomato.append(list(map(int, sys.stdin.readline().split())))
    for j in range (hor):
        if tomato[i][j] == 1:
            rotten.append((i, j))

if len(rotten) == hor * ver:
    print(0)
    exit()

def bfs(a, b):
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < ver and 0 <= ny < hor:
                if tomato[nx][ny] == 0:
                    queue.append((nx, ny))
                    tomato[nx][ny] = tomato[x][y] + 1

a, b = rotten[0]
print(rotten[0])
bfs(a, b)

for i in range(ver):
    print(max(tomato[i]))
    days = max(max(tomato[i]), days)
    for j in range(hor):
        if tomato[i][j] == 0:
            print(-1)
            exit()

print(tomato)
print(days - 1)