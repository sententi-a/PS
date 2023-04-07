# 돌 게임 https://www.acmicpc.net/problem/9655

"""
탁자 위에 돌 N개가 있고, 상근이와 창영이가 번갈아가며 돌을 1개 / 3개 가져감
마지막 돌을 가져가는 사람이 게임을 이김

상근이 먼저 게임 시작, 이기는 사람 구하기
상근 : SK, 창영 : CY 
"""

import sys 

n = int(sys.stdin.readline())

# 돌이 홀수개라면 무조건 상근이가 이김 
# 돌이 짝수개라면 무조건 창영이가 이김

if n & 1:
    print('SK')
else:
    print('CY')