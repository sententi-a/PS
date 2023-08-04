# 수들의 합2 https://www.acmicpc.net/problem/2003

"""
N개로 된 수열이 있을 때, 이 수열의 i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수 구하기
"""

import sys


def solution(num_cnt: int, goal: int, sequence: list):
    answer = 0
    # goal 보다 작거나 같으면 end + 1
    # goal 보다 크면 start + 1
    start, end = 0, 1

    while start <= end and end <= num_cnt:
        total = sum(sequence[start:end])

        if total < goal:
            end += 1

        elif total > goal:
            start += 1

        else:
            answer += 1
            end += 1

    return answer


def solution_faster(num_cnt, goal, sequence):
    answer = 0
    total = 0
    end = 0

    for start in range(num_cnt):
        while total < goal and end < num_cnt:
            total += sequence[end]
            end += 1

        if total == goal:
            answer += 1

        total -= sequence[start]

    return answer


num_cnt, goal = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

print(solution_faster(num_cnt, goal, sequence))
