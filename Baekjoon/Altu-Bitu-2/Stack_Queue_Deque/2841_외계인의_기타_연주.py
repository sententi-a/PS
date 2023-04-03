# 외계인의 기타 연주 https://www.acmicpc.net/problem/2841

"""
기타는 1-6번 줄이 있고, 각 줄은 P개의 프렛으로 나누어짐
프렛의 번호 또한 1번부터 P번까지 나누어짐
각 음은 줄에서 해당하는 프렛을 누르고 줄을 튕기면 연주 가능
만약, 어떤 줄의 프렛을 여러 개 누르고 있다면, 가장 높은 프렛의 음이 발생

어떤 멜로디가 주어졌을 때, 손가락을 가장 적게 움직이는 횟수 구하기
"""

import sys
from collections import defaultdict
import heapq

n, p = map(int, sys.stdin.readline().split())
melody = [] # melody input
pushing_per_line = defaultdict(list)

for _ in range(n):
    melody.append(tuple(map(int, sys.stdin.readline().split())))

finger_move_cnt = 0 


for i in range(n):
    line, prat = melody[i][0], melody[i][1]
    
    # 해당 줄에 누르고 있는 프렛이 있을 때 
    if len(pushing_per_line[line]) != 0:

        while pushing_per_line[line]:
            highest = heapq.heappop(pushing_per_line[line])
            # finger_move_cnt += 1
            
            if prat > -highest:
                heapq.heappush(pushing_per_line[line], highest)
                heapq.heappush(pushing_per_line[line], -prat)
                finger_move_cnt += 1
                # print(prat, highest, finger_move_cnt)
                break

            elif prat < -highest:
                finger_move_cnt += 1
                # print(prat, highest, finger_move_cnt)
                continue

            elif prat == -highest:
                heapq.heappush(pushing_per_line[line], highest)
                # print(prat, highest, finger_move_cnt)
                # finger_move_cnt -= 1
                break
    
    # 원래 누르고 있던 손을 다 뗐을 때
    if len(pushing_per_line[line]) == 0:
        heapq.heappush(pushing_per_line[line], -prat)
        finger_move_cnt += 1
        # print(prat, finger_move_cnt)
        

print(finger_move_cnt)

# 이미 누르고 있고, 가장 높은 음이다 -> 움직임 없음
# 이미 누르고 있는데, 가장 높은 음이 아니다 -> 가장 높은 음이 될 때까지 pop
# 안 누르고 있고, 가장 높은 음이다 -> 그냥 누르기만
# 안 누르고 있고, 가장 높은 음이 아니다 -> 이 숫자 이상의 프렛에서 손 뗄 때까지 pop

# 그럼 정렬을 계속 시켜줘야 하는데, O(n)은 비효율적 -> 우선순위큐?
