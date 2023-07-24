# 분해합 https://www.acmicpc.net/problem/2231

"""
N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
M의 분해합이 N인 경우 M을 N의 생성자라 한다. 
N의 가장 작은 생성자를 구하라.
"""

import sys


num = int(sys.stdin.readline())

answer = 0

digit = len(list(str(num)))

start = num - 9 * digit if num - 9 * digit > 0 else 1

for target in range(start, num + 1):
    target_list = list(map(int, str(target)))
    total = target + sum(target_list)

    if total == num:
        answer = target
        break

print(answer)
