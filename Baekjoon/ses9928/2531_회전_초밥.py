# 회전 초밥 https://www.acmicpc.net/problem/2531

"""
1. 원래는 먹은 초밥만큼 식대 계산, 
그러나 벨트의 임의의 한 위치부터 k개의 접시를 
연속해서 먹을 경우 할인된 정액 가격으로 제공

2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고,
1번 행사에 참가할 경우 쿠폰에 적힌 종류의 초밥 하나를 추가 무료 제공
현재 벨트 위에 없을 경우 요리사가 새로 만들어 손님에게 제공

손님이 먹을 수 있는 초밥 가짓수(개수 아님)의 최댓값 구하기
"""

import sys 
from collections import Counter

plate_cnt, sushi_types, chain_cnt, coupon_num = map(int, sys.stdin.readline().split())
sushis = []
answer = 0

for _ in range(plate_cnt):
    sushis.append(int(sys.stdin.readline()))

# sliding window 
ate = Counter(sushis[:chain_cnt])
answer = len(ate)

# 가장 앞에 있던 초밥을 지우고, 
# 가장 뒤에 있던 초밥보다 한 칸 뒤에 있는 초밥을 추가 
for i in range(1, plate_cnt):
    prev = sushis[i - 1]
    nxt = i + chain_cnt - 1

    if nxt >= plate_cnt:
        nxt -= plate_cnt

    nxt = sushis[nxt]

    # 회전 초밥 제거
    ate[prev] -= 1

    if ate[prev] <= 0:
        del ate[prev]
    
    # 회전 초밥 추가 
    ate[nxt] += 1

    # 쿠폰 
    ate[coupon_num] = 1

    # 최댓값 갱신
    if len(ate) > answer:
        answer = len(ate)

print(answer)
