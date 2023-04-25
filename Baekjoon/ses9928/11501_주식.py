# 주식 https://www.acmicpc.net/problem/11501

"""
매일 한 가지 행동을 함 
1. 주식 하나를 삼
2. 원하는 만큼 가지고 있는 주식을 팖
3. 아무것도 안 함
날별로 주식의 가격을 입력받았을 때, 최대 이익이 얼마나 되는지 계산 
"""

import sys 

tc_cnt = int(sys.stdin.readline())

for _ in range(tc_cnt):
    day_cnt = int(sys.stdin.readline())

    prices = list(map(int, sys.stdin.readline().split()))
    max_price = 0
    answer = 0

    for i in range(day_cnt-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            answer += (max_price - prices[i])
            pass

    print(answer)

