# 볼 모으기 https://www.acmicpc.net/problem/17615

"""
볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 함
1. 바로 옆에 다른 색의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있음
2. 옮길 수 있는 볼의 색깔은 한 가지임
최소 이동 횟수 찾기 (공 개수 <= 500,000)
"""

import sys

ball_cnt = int(sys.stdin.readline())
balls = list(sys.stdin.readline().rstrip())

red, blue = [], []
is_red_first, is_blue_first = balls[0] == 'R', balls[0] == 'B'
is_red_last, is_blue_last = balls[-1] == 'R', balls[-1] == 'R'
answer = sys.maxsize

for i in range(ball_cnt):
    if balls[i] == 'R':
        red.append(i)
    else:
        blue.append(i)


def move_front(target: list, another: list):
    last_adj = 0
    # 가장 앞의 공과 인접한 공들을 제외한, 뒤쪽의 공들을 셈
    for i in range(1, len(target)):
        if target[i] - target[i-1] != 1:
            last_adj = i
            break
    # 여기에서 옮겨야 하는 공과, 다른 색의 공의 개수를 비교하고, 더 작은 숫자를 cnt로 삼아야 함 
    # 예를 들어, BBRBBBBBB의 경우 B 2개를 옮기는 것보다 R 1개를 옮기는 게 효율적
    return min(len(target) - last_adj, len(another))

def move_back(target: list, another: list):
    last_adj = 0
    for i in range(len(target)-1, 0, -1):
        if target[i] - target[i-1] != 1:
            last_adj = i
            break
    return min(last_adj, len(another))


# 빨간 공을 앞쪽으로 몰아야 한다면
cnt = 0

if is_red_first:
    cnt = move_front(red, blue)

# 파란 공을 앞쪽으로 몰아야 한다면 
else:
    cnt = move_front(blue, red)

if answer > cnt:
    answer = cnt
 

# 빨간 공을 뒤쪽으로 몰아야 한다면
cnt = 0

if is_red_last:
    cnt = move_back(red, blue)

# 파란 공을 뒤쪽으로 몰아야 한다면
else: 
    cnt = move_back(blue, red)

if answer > cnt:
    answer = cnt

print(answer)