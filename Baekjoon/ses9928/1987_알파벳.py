# 알파벳 https://www.acmicpc.net/problem/1987

"""
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있음 
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 1행 1열에는 말이 놓임 
말은 상하좌우 중 한 칸으로 이동 가능, 같은 알파벳이 적힌 칸을 두 번 지나갈 수 없음
말이 최대한 몇 칸을 지날 수 있는지 구하기 
"""

import sys 

row, col = map(int, sys.stdin.readline().split())
board = []

for _ in range(row):
    board.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
alphabets = [False for _ in range(ord('Z')-ord('A')+1)]
alphabets[ord(board[0][0]) - ord('A')] = True


def dfs(x, y, count):
    global row, col, answer

    if count > answer:
        answer = count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < row and 0 <= ny < col and not alphabets[ord(board[nx][ny]) - ord('A')]:
            idx = ord(board[nx][ny]) - ord('A')
            alphabets[idx] = True
            dfs(nx, ny, count + 1)
            alphabets[idx] = False


dfs(0, 0, 1)

print(answer)