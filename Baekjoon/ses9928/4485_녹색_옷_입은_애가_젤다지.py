# 녹색 옷 입은 애가 젤다지? https://www.acmicpc.net/problem/4485

"""
링크는 현재 [0][0]번 칸에 위치하고, [N-1][N-1]까지 이동해야 함
동굴의 각 칸마다 도둑 루피가 있는데, 이 칸을 지나가는 걸 최소로 해 이동해야 함
한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있음
링크가 잃을 수밖에 없는 최소 금액은?

항상 인접한 지점에서 적은 금액을 선택하는 게 최소 금액을 보장할 수 있을까? -> 그럼 우선순위큐 사용 가능
보장할 수 없다면 -> 백트래킹 dfs
"""

import sys
from heapq import heappop, heappush

tc_cnt = 1
answers = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 1) dfs를 활용한 방법
def dfs(x: int , y: int, cost: int, n: int, candidates: list):
    cost += cave[x][y]
    
    # 3^n^n의 시간복잡도를 피하기 위해 return 조건 추가
    if candidates and cost > min(candidates):
        return

    if x == n-1 and y == n-1:
        candidates.append(cost)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, cost, n, candidates)
                visited[nx][ny] = False

# 2) 우선순위 큐 활용한 방법 
def go_min_first():
    heap = [(cave[0][0], 0, 0)]

    while heap:
        cost, x, y = heappop(heap)

        if x == n - 1 and y == n - 1:
            return cost

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    heappush(heap, (cost+cave[nx][ny], nx, ny))

    

while True:
    n = int(sys.stdin.readline())

    # 0이 입력되면 입력 종료
    if n == 0:
        print(*answers, sep="\n")
        exit()

    cave = []

    for i in range(n):
        cave.append(list(map(int, sys.stdin.readline().split())))

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    # candidates = []
    # dfs(0, 0, 0, n, candidates)
    
    answers.append(f"Problem {tc_cnt}: {go_min_first()}")

    tc_cnt += 1

