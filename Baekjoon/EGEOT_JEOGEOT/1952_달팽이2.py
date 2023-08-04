# 달팽이2 https://www.acmicpc.net/problem/1952

"""
표의 왼쪽 위 칸 (0, 0)에서 시작해 오른쪽으로 선을 그려나감
표의 바깥 / 이미 그려진 칸에 닿아 더 이상 이동할 수 없게 되면, 시계 방향으로 선을 꺾어서 그려나감 
표의 모든 칸이 채워질 때까지 선을 몇 번 꺾을까?
"""

import sys

row, col = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(col)] for _ in range(row)]
visited[0][0] = True


def check(x: int, y: int, row: int, col: int, visited: list, stack: list):
    if (0 <= x < row and 0 <= y < col) and not visited[x][y]:
        stack.append((x, y, direction))
        visited[x][y] = True
        return True

    return False


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
cnt = 0
stack = [(0, 0, 0)]  # x, y, direction

while stack:
    x, y, direction = stack.pop()
    dx, dy = x + directions[direction][0], y + directions[direction][1]

    if not check(dx, dy, row, col, visited, stack):
        direction = (direction + 1) % 4
        dx, dy = x + directions[direction][0], y + directions[direction][1]

        if check(dx, dy, row, col, visited, stack):
            cnt += 1


print(cnt)
