# 상범 빌딩 https://www.acmicpc.net/problem/6593

"""
상범 빌딩은 각 변의 길이가 1인 정육면체로 이루어짐
각 정육면체는 금으로 이루어져 지나갈 수 없거나, 비어있어 지나갈 수 있음

각 칸에서 인접한 6개의 칸으로 1분의 시간을 들여 이동 가능
오로지 출구를 통해서만 탈출 가능

# : 금으로 막힘
. : 비어 있음
S : 시작지점
E : 출구
"""

import sys 
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True: 
    height, col, row = map(int, sys.stdin.readline().split())

    # 입력으로 주어진 세 개의 정수가 모두 0이라면 끝냄
    if not height and not col and not row:
        exit()

    building = [[] for _ in range(height)] 
    queue = deque()
    flag = False # 탈출 플래그 

    for i in range(height):
        for j in range(col):
            building[i].append(list(map(str, sys.stdin.readline().rstrip())))
            for k in range(row):
                if building[i][j][k] == 'S':
                    queue.append((i, j, k))
                    building[i][j][k] = 0
        temp = sys.stdin.readline() # 각 층 사이의 빈 줄 담는 용도 
    
    while queue:
        x, y, z = queue.popleft()
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        
            if 0 <= nx < height and 0 <= ny < col and 0 <= nz < row:
                if building[nx][ny][nz] == '.':
                    queue.append((nx, ny, nz))
                    building[nx][ny][nz] = building[x][y][z] + 1
                
                # 출구를 만났다면 
                elif building[nx][ny][nz] == 'E':
                    flag = True
                    print(f"Escaped in {building[x][y][z] + 1} minute(s).")
                    break
    
    if not flag:
        print("Trapped!")