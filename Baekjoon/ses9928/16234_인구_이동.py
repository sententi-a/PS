# 인구 이동 https://www.acmicpc.net/problem/16234

"""
N*N 크기의 땅, 각 땅에는 나라가 하나씩 존재
r행 c열에 있는 나라에는 A[r][c]명이 삶 

인구 이동 (하루 동안 진행, 불가능할 때까지)
- L<= 국경선 공유하는 두 나라의 인구 차이 <=R 라면 국경선을 하루 동안 엶
- 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동 시작
- 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있다면, 그 나라를 오늘 하루 동안은 연합이라고 부름
- 연합을 이루는 각 칸의 인구수는 (연합의 인구수)/(연합을 이루는 칸의 개수) 소수점은 버림
- 연합을 해체하고 모든 국경선을 닫음

각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하기
"""

import sys
sys.setrecursionlimit(10**6)

n, minimum, maximum = map(int, sys.stdin.readline().split())
ppl = []

for _ in range(n):
    ppl.append(list(map(int, sys.stdin.readline().split())))

# 비교해야 할 위치 : x좌표 -1, +1, y좌표 -1, +1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

days = 0 # 인구 이동이 발생하는 일수

def dfs(x: int, y: int, stack: list):
    global n, minimum, maximum

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 아직 앞에서 방문하지 않았고, 나라 간 인구 차이가 L명 이상, R명 이하라면 연합을 맺음
        if 0 <= nx < n and 0 <= ny < n:
            if not checked[nx][ny] and minimum <= abs(ppl[x][y] - ppl[nx][ny]) <= maximum:
                stack.append((nx, ny, ppl[nx][ny]))
                checked[nx][ny] = True
                dfs(nx, ny, stack)


while True:
    unions = []
    checked = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i%2, n, 2):
            if not checked[i][j]:
                stack = [(i, j, ppl[i][j])]
                checked[i][j] = True
                dfs(i, j, stack)
                
                if len(stack) > 1:
                    unions.append(stack)

    # 연합이 없다면 인구이동 발생하지 않음
    if not unions:
        break
    
    # 연합이 있다면 연합국들의 인구수를 통일
    for union in unions:
        population = [elem[2] for elem in union]
        avg = sum(population) // len(union)

        for country in union:
            x, y, p = country
            ppl[x][y] = avg

    days += 1


print(days)