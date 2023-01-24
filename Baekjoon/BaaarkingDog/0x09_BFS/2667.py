# 단지번호붙이기 https://acmicpc.net/problem/2667

"""
상하좌우로 연결된 집의 모임인 단지수, 
각 단지에 속하는 집의 수를
오름차순으로 정렬하여 출력
"""

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = int(sys.stdin.readline()) # 지도의 크기
apt = []
answers = [] # 각 단지에 속하는 집의 수 담는 리스트
queue = deque() # BFS를 돌리기 위한 큐

for i in range(size):
    apt.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs():
    global size
    count = 1 # 단지 내 집의 수 

    while queue:
        x, y = queue.popleft()
        apt[x][y] = -1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if apt[nx][ny] == 1:
                    queue.append((nx, ny))
                    apt[nx][ny] = -1
                    count += 1

    return count


for i in range(size):
    for j in range(size):
        if apt[i][j] == 1:
            queue.append((i, j))
            answers.append((bfs()))

answers.sort()
print(len(answers))
print(*answers, sep="\n")