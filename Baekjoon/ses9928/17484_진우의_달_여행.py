# 진우의 달 여행 (Small) https://www.acmicpc.net/problem/17484

"""
지구와 우주 사이는 N * M 행렬로 나타내고,
각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양

우주선이 움직이는 방향 : 왼쪽 대각선 아래, 바로 아래, 오른쪽 대각선 아래
전에 움직인 방향으로 움직일 수 없음

지구의 어느 위치에서든 출발해 달의 어느 위치든 착륙하면 됨
달 여행에 필요한 최소 연료의 값 출력하기
"""

import sys 

row, col = map(int, sys.stdin.readline().split())
space = []

for _ in range(row):
    space.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 1, 1]
dy = [-1, 0, 1]

def dfs(x: int, y: int, oil: int, pos: int, depth: int):
    global row

    if depth == row - 1:
        result.add(oil)
        return

    for i in range(3):
        if pos == i:
            continue
        
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < row and 0 <= ny < col:
            dfs(nx, ny, oil + space[nx][ny], i, depth + 1)


result = set()

for i in range(col):
    dfs(0, i, space[0][i], 4, 0)

print(min(result))
