# 숫자 할리갈리 게임 https://www.acmicpc.net/problem/20923

"""
N장의 카드로 이루어진 덱을 배분 받고, 게임 시작시 그라운드는 비어있음
도도를 시작으로 도도와 수연이가 차례대로 자신이 가진 덱에서 가장 위에 위치한 카드를 그라운드에 숫자가 보이도록 내려놓음
종을 치는 사람이 그라운드에 나와 있는 카드 더미를 모두 가져감
- 그라운드에 나와 있는 각각의 카드 더미에서 가장 위에 위치한 카드의 숫자 합이 5가 되는 순간 수연이가 종을 침 (그라운드가 비어있으면 안 됨)
- 그라운드에 나와 있는 각각의 카드 더미 중 가장 위의 위치한 카드의 숫자가 5일 때 도도가 종을 침
종을 치면 상대방의 그라운드에 있는 카드 더미를 뒤집어 자신의 덱 아래로 그대로 합친 후, 
자신의 그라운드에 있는 카드 더미 역시 뒤집어 자신의 덱 아래로 그대로 가져와 합침

- 게임 진행 도중 자신의 덱에 있는 카드 수가 0이 되면 상대방 승리
- M번 진행 후 덱에 더 많은 카드를 가진 사람 승리 
- M번 진행 후 덱에 있는 카드의 개수가 같으면 비김

게임을 이긴 사람이 도도라면 do, 수연이라면 su, 비겼을 경우 dosu 출력
"""

import sys
from collections import deque

card_cnt, stages = map(int, sys.stdin.readline().split())
dodo_deq = deque([0 for _ in range(card_cnt)])
suyeon_deq = deque([0 for _ in range(card_cnt)])

dodo_ground = deque()
suyeon_ground = deque()

for i in range(card_cnt - 1, -1, -1):
    dodo_deq[i], suyeon_deq[i] = map(int, sys.stdin.readline().split())

# 게임 진행
for stage in range(stages):
    # 도도가 먼저 그라운드에 카드를 내려놓는다. (리스트 상 가장 뒤에 있는 카드)
    if stage % 2 == 0:
        dodo_ground.append(dodo_deq.popleft())

    # 그 다음 수연이 그라운드에 카드를 내려놓는다.
    else:
        suyeon_ground.append(suyeon_deq.popleft())

    # 덱에 있는 카드가 모두 없어지면 게임을 종료한다.
    if not len(dodo_deq) or not len(suyeon_deq):
        break

    # 각 그라운드 위의 카드의 합이 5라면 수연이 카드를 가져간다.
    dodo_ground_top = 0 if not dodo_ground else dodo_ground[-1]
    suyeon_ground_top = 0 if not suyeon_ground else suyeon_ground[-1]

    if (
        dodo_ground_top + suyeon_ground_top == 5
        and dodo_ground_top != 0
        and suyeon_ground_top != 0
    ):
        suyeon_deq.extend(dodo_ground)
        suyeon_deq.extend(suyeon_ground)

        suyeon_ground.clear()
        dodo_ground.clear()

    elif dodo_ground_top == 5 or suyeon_ground_top == 5:
        dodo_deq.extend(suyeon_ground)
        dodo_deq.extend(dodo_ground)

        suyeon_ground.clear()
        dodo_ground.clear()


answer = ""

if len(dodo_deq) > len(suyeon_deq):
    answer += "do"
elif len(dodo_deq) < len(suyeon_deq):
    answer += "su"
else:
    answer += "dosu"

print(answer)
