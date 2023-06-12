# 좋다 https://www.acmicpc.net/problem/1253

"""
N개의 수 중 어떤 수가 다른 두 수 두 개의 합으로 나타낼 수 있다면 그 수를 좋다고 함
N개의 수 중 좋은 수의 개수가 몇 개인지 출력
수의 위치가 다르면 값이 같아도 다른 수임
"""

import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

good_nums = 0

for i in range(n):
    start, end = 0, n-1

    while start < end:
        # 자기 자신은 빼기 
        if start == i:
            start += 1
            continue 

        if end == i:
            end -= 1
            continue

        total = nums[start] + nums[end]

        if total == nums[i]:
            good_nums += 1
            break

        elif total > nums[i]:
            end -= 1

        else:
            start += 1

print(good_nums)