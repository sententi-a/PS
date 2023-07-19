# 고층 건물 https://www.acmicpc.net/problem/1027

"""
가장 많은 고층 빌딩이 보이는 건물을 찾으려고 함
빌딩은 총 N개, 선분으로 나타냄
- i번째 빌딩은 (i, 0) ~ (i, 높이)의 선분으로 나타낼 수 있음 
고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 
두 지붕을 잇는 선분이 A, B 제외 다른 고층 빌딩을 지나거나 접하지 않아야 함
"""

import sys

building_cnt = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))

if building_cnt == 1 or building_cnt == 2:
    print(building_cnt - 1)
    exit()


def ccw(coord1, coord2, coord3):
    answer = (coord2[0] - coord1[0]) * (coord3[1] - coord1[1]) - (
        coord3[0] - coord1[0]
    ) * (coord2[1] - coord1[1])
    return answer


def validation(start, end, buildings):
    for middle in range(start + 1, end):
        coord1 = (start, buildings[start])
        coord2 = (middle, buildings[middle])
        coord3 = (end, buildings[end])

        if ccw(coord1, coord2, coord3) <= 0:
            return False

    return True


max_cnt = 0

# 중간 빌딩들이 두 좌표를 지나는 일차 방정식 직선 기준 아래에 있어야 한다.
# 두 빌딩 사이에 있는 나머지 빌딩을 모두 확인해야 함.
# CCW 알고리즘 사용해서 반시계 방향이면 통과 (양수)
# 그러나 중간 빌딩과 연산했을 때 하나라도 시계 방향이거나 일직선 상에 있으면 (0이하) 두 빌딩은 서로 보이지 않음
for target in range(building_cnt):
    cnt = 0
    first, last = target, target
    for end in range(target - 1, -1, -1):
        if validation(end, target, buildings):
            cnt += 1
            first = end

    for end in range(target + 1, building_cnt):
        if validation(target, end, buildings):
            cnt += 1
            last = end

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
