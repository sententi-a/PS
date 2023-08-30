# 톱니 바퀴 https://www.acmicpc.net/problem/14891

"""
1, 2, 3, 4번 톱니바퀴, 각각 총 8개의 톱니를 가짐 
톱니바퀴를 총 K번 회전 (시계: 1 / 반시계: -1) 
맞닿은 극이 서로 다를 때, 인접한 톱니바퀴가 회전하는 반대 방향으로 회전함 

12시 방향부터 시계 방향 순서대로 톱니바퀴의 상태가 주어짐 (N: 0, S: 1)
"""

import sys


def get_prev_idx(idx: int, gap: int):
    idx -= gap

    if idx < 0:
        idx = 8 + idx

    return idx


def get_next_idx(idx: int, gap: int):
    idx += gap

    if idx > 7:
        idx -= 8

    return idx


def rotate(gear: int, direction: int, pole_idxs: list):
    if direction == 1:
        pole_idxs[gear] = get_prev_idx(pole_idxs[gear], 1)
    else:
        pole_idxs[gear] = get_next_idx(pole_idxs[gear], 1)

    return


# 톱니바퀴의 상태
gears = [""]

for _ in range(4):
    gears.append(sys.stdin.readline().rstrip())

# n번 톱니바퀴의 12시 방향 인덱스들
pole_idxs = [0 for _ in range(5)]

# 회전 방법
for _ in range(int(sys.stdin.readline())):
    num, direction = map(int, sys.stdin.readline().split())

    # 회전 대상인지 아닌지 담는 리스트
    is_target = [False for _ in range(5)]
    is_target[num] = True
    # 회전 방향을 담는 리스트
    directions = [direction for _ in range(5)]

    for left in range(num - 1, 0, -1):
        # left + 1의 왼쪽 방향, left의 오른쪽 부분이 다를 때 회전
        if (
            gears[left][get_next_idx(pole_idxs[left], 2)]
            != gears[left + 1][get_prev_idx(pole_idxs[left + 1], 2)]
        ):
            is_target[left] = True
            directions[left] = direction * ((-1) ** (num - left))
        else:
            break

    for right in range(num + 1, 5):
        # right - 1의 오른쪽 방향, right의 왼쪽 부분이 다를 때 회전
        if (
            gears[right][get_prev_idx(pole_idxs[right], 2)]
            != gears[right - 1][get_next_idx(pole_idxs[right - 1], 2)]
        ):
            is_target[right] = True
            directions[right] = direction * ((-1) ** (right - num))
        else:
            break

    # 실질적으로 회전을 시킴
    for gear in range(1, 5):
        if is_target[gear]:
            rotate(gear, directions[gear], pole_idxs)


answer = 0

for i in range(1, 5):
    answer += (2 ** (i - 1)) * int(gears[i][pole_idxs[i]])

print(answer)
