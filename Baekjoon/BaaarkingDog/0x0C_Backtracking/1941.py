# 소문난 칠공주 https://acmicpc.net/problem/1941

"""
소문난 칠공주 구성 조건
- 7명의 학생으로 구성
- 7명의 자리는 서로 가로나 세로로 인접
- '임도연파(Y)' 혹은 '이다솜파(S)'로 구성
- 생존을 위해 '이다솜파'의 학생이 적어도 4명 이상이어야 함
자리 배치도가 주어졌을 때, '소문난 칠공주'를 결성할 수 있는 모든 경우의 수 구하기
"""

import sys 

seat = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(5)]
count = 0 # 칠공주를 결성할 수 있는 경우의 수
dx = [-1, 1, 0]
dy = [0, 0, 1]

answer =[None for _ in range(8)]
result = []



def sol(cur, x, y):
    global count

    if cur == 7:
        if answer.count('S') >= 4 and answer[:7] not in result: # 중복 제거
            result.append(answer[:7])
            print(answer[:7])
            count += 1
        return

    # cur == 0일 때 
    if cur == 0:
        answer[cur] = seat[x][y]

    # print(f'재귀가 제대로 이루어짐? {cur} {x}, {y}')
    # x, y = queue.popleft()
    visited[x][y] = True

    for i in range(3):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            # queue.append((nx, ny))
            if cur != 0:
                answer[cur] = seat[nx][ny]
            # print(f"여기 들어옴 {x}, {y}\n")
            # Backtracking의 여지를 남겨줘야 함 딱 한 번 호출 후 끝나는듯
            sol(cur+1, nx, ny)
            visited[nx][ny] = False


for i in range(5):
    for j in range(5):
        visited = [[False for _ in range(5)] for _ in range(5)] 
        # queue.append((i, j))
        sol(0, i, j)

print(count)

    

    
    