# N-Queen https://acmicpc.net/problem/9663

"""
N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓아야 함
- 퀸이 놓였을 때, 자신을 기준으로 가로 세로 대각선 방향에 아무것도 놓여있으면 안 됨
퀸을 놓는 방법의 수 구하기
"""

import sys

n = int(sys.stdin.readline())

count = 0
# queens[1]의 값 : 첫 번째 줄(row)에서의 퀸의 위치(col)
queens = [0 for _ in range(n+1)] 
visited = [False for _ in range(n+1)]

"""
일단 첫 번째 줄에 놓으면, 두 번째 줄로 넘어가야 함 
이후 윗줄 기준으로 +-1 / +1 / 0 이면 안 됨 
"""

def sol(k):
    global n, count
    # Base condition
    if k == n:
        print(queens)
        count += 1
        return
    
    for i in range(1, n+1): # for index 
        if not visited[i]: # 현재 인덱스에 놓여있지 않고
            for j in range(1, n+1): # for value
                if j not in queens:
                    visited[i] = True
                    queens[i] = j
                    sol(k+1)
                    visited[i] = False
                    # queens[i] = 0
                

sol(1)
print(count)