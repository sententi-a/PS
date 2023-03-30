# 패션왕 신해빈 https://www.acmicpc.net/problem/9375

"""
한 번 입었던 옷들의 조합을 절대 다시 입지 않음
해빈이가 가진 의상들이 주어졌을 때, 
알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
"""

import sys
from collections import defaultdict

tc = int(sys.stdin.readline())

for _ in range(tc):
    clothes_cnt = int(sys.stdin.readline())
    clothes_dict = defaultdict(int)

    for _ in range(clothes_cnt):
        cloth, category = sys.stdin.readline().split()
        clothes_dict[category] += 1

    categories_cnt = len(clothes_dict.keys())
    answer = 1 

    for key, value in clothes_dict.items():
        answer *= value + 1

    answer -= 1

    print(answer)
        