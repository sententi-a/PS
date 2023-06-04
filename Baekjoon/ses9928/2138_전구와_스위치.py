# 전구와 스위치 https://www.acmicpc.net/problem/2138

"""
N개의 스위치와 N개의 전구가 있음
i번 스위치를 누르면 i-1, i, i+1 세 개의 전구 상태가 바뀜

N개의 전구들의 현재 상태와, 우리가 만들고자 하는 상태가 주어졌을 때
그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 될까
불가능할 경우 -1 출력 
"""

import sys

bulb = int(sys.stdin.readline())

start = list(map(int, sys.stdin.readline().rstrip()))
goal = list(map(int, sys.stdin.readline().rstrip()))

INF = 10 ** 9

def press_switch(bulbs: list, index: int):
    start, end = index - 1, index + 1

    if index == 0:
        start += 1
    
    elif index == len(bulbs)-1:
        end -= 1

    for i in range(start, end+1):
        bulbs[i] = 1 - bulbs[i]


def walk_switches(start: list, goal: str):
    copy = start[:]
    press_cnt = 0

    for i in range(1, len(copy)):
        if copy[i-1] != goal[i-1]:
            press_switch(copy, i)
            press_cnt += 1

    if copy == goal:
        return press_cnt
        
    return INF


answers = []

# 0번 스위치를 누르지 않았을 때 
answers.append(walk_switches(start, goal))

# 0번 스위치를 눌렀을 때
press_switch(start, 0)
answers.append(walk_switches(start, goal) + 1)

# 정답 출력
if min(answers) == INF:
    print(-1)
else:
    print(min(answers))