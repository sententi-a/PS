# 스도쿠 https://www.acmicpc.net/problem/2580

"""
3*3의 작은 칸이 가로 세로 3개씩 위치
- 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 함
- 3*3 정사각형 안에도 1부터 9까지의 수가 한 번씩만 나타나야 함 
"""

import sys

SIZE = 9
sudoku = []
empty = []

rows = [set([i for i in range(1, 10)]) for _ in range(9)]  # 각 행에 존재하는 숫자들
cols = [set([i for i in range(1, 10)]) for _ in range(9)]  # 각 열에 존재하는 숫자들
squares = [set([i for i in range(1, 10)]) for _ in range(9)]  # 각 3*3 사각형에 존재하는 숫자들


def get_area_num(x: int, y: int):
    return (x // 3) * 3 + y // 3


def backtracking(k):
    # 모든 빈칸을 채웠으면 True를 리턴한다.
    if k == len(empty):
        return True

    x, y = empty[k]

    # 가로, 세로, 정사각형을 살펴보며 적절한 숫자를 찾는다.
    intersect = rows[x].intersection(cols[y].intersection(squares[get_area_num(x, y)]))

    for num in list(intersect):
        # 스도쿠를 채운다.
        rows[x].remove(num)
        cols[y].remove(num)
        squares[get_area_num(x, y)].remove(num)
        sudoku[x][y] = num

        # 진행시킨다.
        # 만약 return True가 없다면 스도쿠에서 다시 숫자가 지워질 것이다.
        # True를 리턴함으로써 해당 칸에 특정 숫자를 넣는게 맞다는 것을 표현한다.
        if backtracking(k + 1):
            return True

        # 다시 그 수를 스도쿠에서 지운다.
        rows[x].add(num)
        cols[y].add(num)
        squares[get_area_num(x, y)].add(num)
        sudoku[x][y] = 0

    # 넣을 수 있는 숫자가 없다면 다시 그 숫자를 지울 수 있도록 False를 리턴한다.
    return False


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(SIZE)]

for i in range(SIZE):
    for j in range(SIZE):
        value = sudoku[i][j]

        if value == 0:
            empty.append((i, j))
            continue

        rows[i].remove(value)
        cols[j].remove(value)
        squares[get_area_num(i, j)].remove(value)

backtracking(0)

for i in range(9):
    print(*sudoku[i], sep=" ")
