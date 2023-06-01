# 스카이라인 쉬운거 https://www.acmicpc.net/problem/1863

"""
도시에서 태양이 질 때 보이는 건물들의 윤곽을 스카이라인이라고 함
스카이라인만을 보고 도시에 세워진 건물이 최소한 몇 채인지 알아내기
건물은 모두 직사각형 모양으로 밋밋하게 생겼다고 가정함
"""

import sys

spot_cnt = int(sys.stdin.readline())
skyline = []

building_cnt = 0


def count_buildings(skyline: list, popped: list):
    global building_cnt

    if not popped[skyline[-1][1]] and skyline[-1][1] != 0:
        building_cnt += 1
        popped[skyline[-1][1]] = True

    skyline.pop()


for i in range(spot_cnt):
    x, y = map(int, sys.stdin.readline().split())

    if i == 0:
        skyline.append((x, y))

    if i > 0:
       popped = [False for _ in range(skyline[-1][1] + 1)]
       
       while True:
            # 이전보다 높이가 낮으면 높이가 크거나 같은 이전 그림자를 찾을 때까지 pop
            # 빌딩 개수를 셀 때 이미 동일한 높이에 대해 계산했으면 더이상 더하지 않음
            if skyline and y < skyline[-1][1]:
                count_buildings(skyline, popped)

            # skyline 리스트에 원소가 없거나 이전 그림자와 높이가 크거나 같을 때 그냥 추가
            else:
                skyline.append((x, y))
                break

# skyline 리스트가 남아있다면 
if skyline:
    popped = [False for _ in range(skyline[-1][1] + 1)]

    while skyline:
        count_buildings(skyline, popped)
            
print(building_cnt)