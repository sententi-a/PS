# 통계학  https://www.acmicpc.net/problem/2108

"""
N (홀수)
1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이 

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램 작성
"""

import sys
# from math import round
from collections import defaultdict

cnt = int(sys.stdin.readline())
nums = []
each_num_cnt = defaultdict(int)

for _ in range(cnt):
    num = int(sys.stdin.readline())
    nums.append(num)
    each_num_cnt[num] += 1

nums.sort()
num_dict = sorted(each_num_cnt.items(), key=lambda x: (-x[1], x[0]))

average = sum(nums) / cnt
if average < 0:
    average = -round(abs(average))
else:
    average = round(average)

middle = len(nums) // 2
mode = 0
if cnt > 1 and num_dict[0][1] == num_dict[1][1]:
    mode = num_dict[1][0]
else:
    mode = num_dict[0][0]
min_num, max_num = nums[0], nums[cnt-1]

print(average)
print(nums[middle])
print(mode)
print(max_num - min_num)
