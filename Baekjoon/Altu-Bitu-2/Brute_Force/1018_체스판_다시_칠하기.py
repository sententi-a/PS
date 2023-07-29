# 체스판 다시 칠하기 https://www.acmicpc.net/problem/1018

"""
MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있음 
이 보드를 잘라 8*8 크기의 체스판으로 만들려고 함
- 검/흰이 번갈아 칠해져 있어야 함
- 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 함

다시 칠해야 하는 정사각형의 최소 개수 구하기
"""

import sys


def count_board(board: list, goal: list, x: int, y: int):
    """
    바꿔야 하는 구역의 개수 중 작은 수를 리턴한다 (B로 시작할 경우와 W로 시작할 경우 모두 count)
    """
    cnt = 0

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if board[i][j] != goal[i - x][j - y]:
                cnt += 1

    return min(cnt, 64 - cnt)


# 완성된 체스판
types = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]
goal = []

for i in range(8):
    goal.append(types[i % 2])


row, col = map(int, sys.stdin.readline().split())
board = []

for _ in range(row):
    board.append(list(sys.stdin.readline().rstrip()))

answer = row * col

# i, j를 시작지점으로 하는 8*8 체스판을 만들고, 다시 칠해야 하는 정사각형 개수 구하기
for i in range(0, row - 8 + 1):
    for j in range(0, col - 8 + 1):
        cnt = count_board(board, goal, i, j)

        if cnt < answer:
            answer = cnt

print(answer)
