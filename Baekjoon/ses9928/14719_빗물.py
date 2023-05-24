# 빗물 https://www.acmicpc.net/problem/14719

"""
2차원 세계에 블록이 쌓여 있고, 비가 오면 블록 사이에 빗물이 고임
비가 충분히 많이 온다고 할 때, 고이는 빗물의 총량은 얼마? 

"""

import sys 

height, width = map(int, sys.stdin.readline().split())
buildings = list(map(int, sys.stdin.readline().split()))

rain = 0
# rain = height * width - buildings[0]
# max_height, idx = buildings[0], 0

# for i in range(1, width):
#     rain -= buildings[i]

#     if max_height <= buildings[i]:
#         empty = (height - max_height) * (i - idx)
#         rain -= empty

#         max_height, idx = buildings[i], i
#     # 가운데에 멈춰야 할 경우 어떻게 할지 생각해보기 
#     elif i == width - 1:
#         if buildings[i] > 0:
#             empty = (height - buildings[i]) * (i - idx)
#             rain -= empty
#         else:
#             rain -= height * (i - idx + 1)

if width <= 2:
    print(0)
    exit()

# left, right를 계속해서 바꿔가기
left, right = 0, 0

while left < width-1:
    right = buildings.index(max(buildings[left+1:]), left+1)
    # print(left, right)

    criteria = min(buildings[left], buildings[right]) 

    for i in range(left+1, right):
        if buildings[i] < criteria:
            rain += criteria - buildings[i]

    left = right


    
# if rain < 0:
#     print(0)

# else:
#     print(rain)

print(rain)