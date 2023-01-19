# 나이트의 이동 https://www.acmicpc.net/problem/7562
"""
나이트가 한 번에 이동할 수 있는 칸
dx = [-1, 1, -2, 2, -2, -1, 1, 2]
dy = [2, 2, 1, 1, -1, -2, -2, -1]
나이트가 이동하려고 하는 칸이 주어진다.
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까? 
"""
import sys 
from collections import deque

dx = [-1, 1, -2, 2, -2, -1, 1, 2]
dy = [2, 2, 1, 1, -1, -2, -2, -1] 

for _ in range(int(sys.stdin.readline())):
    length = int(sys.stdin.readline()) # 체스판 한 변의 길이
    curr = tuple(map(int, sys.stdin.readline().split())) # 현재 위치
    goal = tuple(map(int, sys.stdin.readline().split())) # 목표 위치

    count = 0 # 최소 몇 번만에 이동할 수 있는지
    visited = [[-1 for _ in range(length)] for _ in range(length)]
    queue = deque([curr])
    visited[curr[0]][curr[1]] = 0 # 시작 위치는 0으로 둠

    while queue:
        x, y = queue.popleft()

        if x == goal[0] and y == goal[1]:
            count = visited[x][y]
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < length and 0 <= ny < length:
                if visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    print(count)