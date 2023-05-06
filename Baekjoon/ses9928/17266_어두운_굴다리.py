# 어두운 굴다리 https://www.acmicpc.net/problem/17266

"""
0-N까지의 거리를 모두 밝히기 위한 가로등의 최소 높이
"""

import sys
from math import ceil

length = int(sys.stdin.readline())
lamp_cnt = int(sys.stdin.readline())
lamps = list(map(int, sys.stdin.readline().split()))

height = 0

# 맨 앞, 맨 뒤는 온전히 가로등 하나로 커버해야 하므로 최소한 거리만큼의 높이를 가져야 함
height = max(lamps[0],  length - lamps[-1])

# 가로등과 가로등 사이는 ceil(거리 / 2) 만큼만 비춰주면 됨
for i in range(1, lamp_cnt):
    temp_height = ceil((lamps[i] - lamps[i-1]) / 2)

    if temp_height > height:
        height = temp_height


print(height)