# 카드 놓기 https://www.acmicpc.net/problem/18115

"""
1. 제일 위의 카드 1장을 바닥에 내려놓음 
- 즉, 제일 위의 카드보다 위에 넣기
2. 위에서 두 번째 카드를 바닥에 내려놓음 (2장 이상일 때)
- 즉, 제일 위의 카드보다 위에서 두 번째에 넣기
3. 제일 밑에 있는 카드를 바닥에 내려놓음 (2장 이상일 때)
- 제일 위의 카드 바로 밑에 넣기

카드를 다 내려놓았을 때, 놓여 있는 카드들을 확인했더니 
위에서부터 순서대로 1, 2, ... , N이 적혀 있었음 (1이 가장 마지막으로 놓여짐)

A[i] = x : i번째로 카드를 내려놓을 때 x번 기술을 씀
처음 카드가 어떻게 배치되어 있었을까
"""

import sys
from collections import deque

cnt = int(sys.stdin.readline())

cards = [i for i in range(cnt, 0, -1)]
missions = list(map(int, sys.stdin.readline().split()))
origin = deque()

# [4, 3, 2, 5, 1] (아래 -> 위)
# 2, 3, 3, 2, 1 작업 후 -> [5, 4, 3, 2, 1] (아래 -> 위)
# 거꾸로 생각해야함! 다시 넣기

for i in range(cnt-1, -1, -1):
    # 첫 번째 기술
    if missions[i] == 1:
        origin.appendleft(cards[i])
    # 두 번째 기술 (위에서 두 번째)
    elif missions[i] == 2:
        origin.insert(1, cards[i])
    # 세 번째 기술 (가장 밑)
    else: 
        origin.append(cards[i])


print(*origin)
