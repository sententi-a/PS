# 수열 https://www.acmicpc.net/problem/2559

"""
매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때,
연속적인 며칠 동안의 온도의 합이 가장 큰 값 찾기 
"""

import sys

days, consecutive = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

total = sum(temperatures[:consecutive])
answer = total

for start in range(days - consecutive):
    end = start + consecutive

    total = total - temperatures[start] + temperatures[end]

    if total > answer:
        answer = total

print(answer)
