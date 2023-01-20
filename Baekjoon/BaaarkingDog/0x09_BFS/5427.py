# 불 https://acmicpc.net/problem/5427

"""
매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼짐 
상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없음
상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있음
상근이가 얼마나 빨리 빌딩을 탈출할 수 있는지 구하기
. : 빈 공간
# : 벽
@ : 상근이의 시작 위치
* : 불
"""

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(sys.stdin.readline())):
    building = []
    queue = deque()
    answer = 0

    row, col = map(int, sys.stdin.readline().split())

    f_visited = [[0 for _ in range(row)] for _ in range(col)]
    s_visited = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(col):
        building.append(list(map(str, sys.stdin.readline().rstrip())))
        for j in range(row):
            # 불일 경우 
            if building[i][j] == '*':
                queue.append((i, j))
                f_visited[i][j] = 1
            # 상근이일 경우
            elif building[i][j] == '@':
                queue.append((i, j))
                s_visited[i][j] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 상근이가 탈출했을 경우
            if nx < 0 or nx >= col or ny < 0 or ny >= row:
                if building[x][y] == '@':
                    answer = s_visited[x][y]
                    break
                
            elif 0 <= nx < col and 0 <= ny < row:
                # 불 이동
                # if building[x][y] == '*':
                if f_visited[x][y] > 0:
                    if f_visited[nx][ny] == 0 and building[nx][ny] != '#':
                        queue.append((nx, ny))
                        f_visited[nx][ny] = f_visited[x][y] + 1
                        # if building[nx][ny] == '@'
                        building[nx][ny] = '*'
                
                # 상근 이동
                if s_visited[x][y] > 0:
                # elif building[x][y] == '@':
                    if s_visited[nx][ny] == 0 and building[nx][ny] == '.':
                        # 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없음 (그 반대면 이동)
                        if f_visited[nx][ny] == 0 or s_visited[x][y] + 1 < f_visited[nx][ny]:  
                            queue.append((nx, ny))
                            s_visited[nx][ny] = s_visited[x][y] + 1
                            building[nx][ny] = '@'
                            building[x][y] = '.'
            # else:
            #     # print(f"들어옴 {building[x][y]}\n")
            #     if building[x][y] == '@':
            #         print(s_visited[x][y] + 1)
            #         break
    if answer == 0:
        print('IMPOSSIBLE')

    else:
        print(answer)
    