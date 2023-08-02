# 시험 감독 https://www.acmicpc.net/problem/13458

"""
N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있음
i번 시험장에 있는 응시자의 수 : Ai
총감독관 : 한 시험장에서 감시할 수 있는 응시자의 수가 B명 
부감독관 : 한 시험장에서 감시할 수 있는 응시자의 수가 C명 

각각의 시험장에 총감독관은 오직 1명, 부감독관은 여러 명 있어도 됨
모든 응시생들을 감시해야할 때, 필요한 총 감독관 수의 최솟값 구하기
"""

import sys
from math import ceil

room_cnt = int(sys.stdin.readline())
rooms = list(map(int, sys.stdin.readline().split()))

general, deputy = map(int, sys.stdin.readline().split())

answer = 0

for i in range(room_cnt):
    # 부감독관도 필요한 경우
    if rooms[i] - general > 0:
        cnt = 1 + ceil((rooms[i] - general) / deputy)
    # 총감독관만으로 커버 가능한 경우
    else:
        cnt = 1

    answer += cnt

print(answer)
