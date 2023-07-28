# 블랙잭 https://www.acmicpc.net/problem/2798

"""
원래 규칙 : 숫자의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만들기 
- 각 카드에는 양의 정수가 쓰여 있음
- 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓음
- 딜러는 숫자 M을 크게 외침

- 플레이어는 제한 시간 안에 N장의 카드 중 3장의 카드를 골라야 함
- 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 함 
"""

import sys
from itertools import combinations

card_cnt, goal = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

answer = 0

for comb in combinations(cards, 3):
    sum_of_cards = sum(comb)

    if answer < sum_of_cards <= goal:
        answer = sum_of_cards

print(answer)
