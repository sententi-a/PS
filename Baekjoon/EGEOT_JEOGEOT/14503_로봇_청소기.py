# 로봇 청소기 https://www.acmicpc.net/problem/14503

"""
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수 구하기
1 * 1의 정사각형으로 나누어진 N * M 크기의 방으로 각각의 칸은 벽 / 빈칸
청소기는 바라보는 방향이 있음 (동, 서, 남, 북)
방의 각 칸은 좌표 (r, c)로 나타낼 수 있음

1. 현재 칸이 아직 청소되지 않은 경우 현재 칸 청소
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없을 때 
    - 바라보는 방향을 유지한 채 한 칸 후진할 수 있다면 한 칸 후진 후 1번으로 돌아감
    - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    - 반시계 방향으로 90도 회전
    - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        - 청소된 빈 칸인 경우 또 반시계 방향으로 90도 회전 후 확인
    - 1번으로 돌아감 

0 : 청소되지 않은 빈 칸 / 1 : 벽
"""

import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
start_x, start_y, start_d = map(int, sys.stdin.readline().split())
graph = []

for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 방향 배열 (북, 동, 남, 서)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 경로 담는 큐
queue = deque([(start_x, start_y, start_d)])

# 청소하는 칸의 개수
answer = 0

while queue:
    x, y, direction = queue.popleft()

    # 1. 현재 칸이 청소되지 않은 경우, 현재 칸 청소
    if graph[x][y] == 0:
        graph[x][y] = 2
        answer += 1

    # --- 청소되지 않은 빈 칸 추가 --- #
    not_cleaned_empty = []

    for _ in range(4):
        # 과정3을 위해 반시계 방향으로 append
        direction = direction - 1 if direction - 1 >= 0 else 3
        dx, dy = x + dirs[direction][0], y + dirs[direction][1]

        if (0 <= dx < row and 0 <= dy < col) and graph[dx][dy] == 0:
            not_cleaned_empty.append((dx, dy, direction))

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없을 때
    if not not_cleaned_empty:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아감
        dx, dy = x + -dirs[direction][0], y + -dirs[direction][1]

        if graph[dx][dy] != 1:
            queue.append((dx, dy, direction))

        # 후진할 수 없다면 작동을 멈춤
        else:
            break

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 청소 안 한 곳을 만날 때까지 반 시계 방향으로 90도 회전 (이미 추가할 때부터 반시계 방향으로 회전 후 추가됨)
        for elem in not_cleaned_empty:
            dx, dy, new_dir = elem

            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            if graph[dx][dy] == 0:
                queue.append(elem)
                break

print(answer)
