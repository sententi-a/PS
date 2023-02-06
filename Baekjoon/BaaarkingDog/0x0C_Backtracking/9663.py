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
queens = [None for _ in range(n)] 
placed = [False for _ in range(n)] # 특정 col에 퀸을 놓았는지 여부

"""
일단 첫 번째 줄에 놓으면, 두 번째 줄로 넘어가야 함 
이후 윗줄 기준으로 +-1 / +1 / 0 이면 안 됨 
"""

def pos_check(cur):
    for j in range(cur):
        if queens[cur] == queens[j] or abs(cur-j) == abs(queens[cur]-queens[j]):
            return False
    return True

def sol(cur):
    # cur : 현재 내가 퀸을 놓으려는 row
    global n, count

    # Base condition
    if cur == n:
        # print(queens)
        count += 1
        return
    
    # 어떤 column에 놓을지 정함
    for i in range(n):
        if placed[i]:
            continue

        queens[cur] = i

        # position check 
        if pos_check(cur):
            placed[i] = True
            sol(cur+1)
            placed[i] = False
     
                

sol(0)
print(count)