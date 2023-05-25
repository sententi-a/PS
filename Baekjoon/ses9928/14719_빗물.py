# 빗물 https://www.acmicpc.net/problem/14719

"""
2차원 세계에 블록이 쌓여 있고, 비가 오면 블록 사이에 빗물이 고임
비가 충분히 많이 온다고 할 때, 고이는 빗물의 총량은 얼마? 
"""

import sys 

height, width = map(int, sys.stdin.readline().split())
buildings = list(map(int, sys.stdin.readline().split()))

rain = 0

if width <= 2:
    print(0)
    exit()

def find_right_wall(left: int, end: int, buildings: list):
    right = left + 1
    # max_in_range = max(buildings[right:])

    for i in range(right, end):
        # left 건물보다 right 건물의 높이가 크거나 같을 때 
        if buildings[left] <= buildings[i]:
            return i
        # left 건물보다 right 건물의 높이는 낮다면, 그 중에서도 가장 높은 건물을 찾아야 함
        if buildings[right] < buildings[i]:
            right = i
    
    return right

def calculate_rain_amount(left: int, right: int, buildings: list, criteria: int):
    cnt = 0 

    for i in range(left+1, right):
        cnt += criteria - buildings[i]
    
    return cnt

# left, right를 계속해서 바꿔가기
left, right = 0, 0

while left < width-1:
    right = find_right_wall(left, width, buildings)

    criteria = min(buildings[left], buildings[right]) 

    rain += calculate_rain_amount(left, right, buildings, criteria)

    left = right


print(rain)