# 영역 구하기 https://www.acmicpc.net/problem/2583

"""
눈금의 간격이 1인 M x N 크기의 모눈종이 
모눈종이 위 눈금에 맞춰 K개의 직사각형을 그릴 때, 
K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어짐

몇 개로 나누어지는지, 분리된 각 영역의 넓이가 얼마인지 구해 출력
"""

import sys 
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

col, row, rect = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(row)] for _ in range(col)]


for _ in range(rect):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
    

def bfs():
    global col, row
    count = 1

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < col and 0 <= ny < row:
                if graph[nx][ny] == 0:
                    count += 1
                    queue.append((nx, ny))
                    graph[nx][ny] = 1
    return count

answers = [] # 분리되는 각 영역의 넓이 저장하는 리스트
queue = deque() 

for i in range(col):
    for j in range(row):
        if graph[i][j] == 0:
            queue.append((i, j))
            answers.append(bfs())

answers.sort() # 오름차순으로 정렬

print(len(answers)) # 나누어지는 영역의 개수
print(*answers) 