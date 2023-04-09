# 임스와 함께하는 미니게임 https://www.acmicpc.net/problem/25757

"""
Y(윳놀이) : 2명, F(같은그림찾기): 3명, O(원카드): 4명
-> 인원 수 부족할 시 게임 시작 불가
N : 플레이 신청 횟수 
최대 몇 번이나 임스와 함께 게임을 할 수 있는지 구하기

한 번 같이 플레이한 사람과 다시 플레이하지 않음, 동명이인 X
"""

import sys 

n, game = sys.stdin.readline().split()
n = int(n)
players = set()

for _ in range(n):
    players.add(sys.stdin.readline().rstrip())

# 윳놀이
if game == 'Y':
    print(len(players))

# 같은그림찾기
elif game == 'F':
    print(len(players) // 2)
# 원카드 
else:
    print(len(players) // 3)
