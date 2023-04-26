# 창고 다각형 https://www.acmicpc.net/problem/2304

"""
창고의 지붕을 만들려고 함
1. 지붕은 수평 부분/수직 부분으로 구성되고, 모두 연결되어야 함
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 함
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 함
4. 지붕의 가장자리는 땅에 닿아야 함 
5. 비가 올 때 물이 고이지 않게 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 함

창고 다각형의 면접이 가장 작은 창고 만들고, 그 때의 면적 구하기
"""

import sys

roof_cnt = int(sys.stdin.readline())
roofs = [[0, 0] for _ in range(roof_cnt)]

for i in range(roof_cnt):
    _input = list(map(int, sys.stdin.readline().split()))
    roofs[i][0], roofs[i][1] = _input[0], _input[1]
    

roofs.sort()

# 기둥 중 가장 높은 기둥의 높이와 인덱스를 구함
max_height, max_idx = 0, 0

for i in range(roof_cnt):
    if roofs[i][1] > max_height:
        max_height = roofs[i][1]
        max_idx = i

area = max_height

# max를 기준으로 앞부분은 처음부터 계산, 뒷부분은 뒤부터 계산
# 이전에 봤던 기둥보다 더 높은 기둥의 높이를 갱신하면서 해당 높이 * 폭 값을 계속 더해줌
max_front = 0

for i in range(max_idx):
    if max_front < roofs[i][1]:
        max_front = roofs[i][1]
    area += max_front * (roofs[i+1][0] - roofs[i][0])
    # print(i, max_front, area)

max_back = 0

for i in range(roof_cnt-1, max_idx, -1):
    if max_back < roofs[i][1]:
        max_back = roofs[i][1]
    area += max_back * (roofs[i][0] - roofs[i-1][0])
    # print(i, max_back, area)

print(area)
