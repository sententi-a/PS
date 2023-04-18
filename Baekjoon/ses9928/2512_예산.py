# 예산 https://www.acmicpc.net/problem/2512

"""
정해진 총액 이하에서 가능한 한 최대의 총 예산을 배정
1. 모든 요청이 배정될 수 있으면 그대로 배정
2. 없으면 정수 상한액을 계산해, 그 이상인 예상 요청에는 모두 상한액 배정

배정된 예산들 중 최댓값인 정수 구하기
"""

import sys 
from bisect import bisect_left

region_cnt = int(sys.stdin.readline())
requirements = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())
answer = 0

if sum(requirements) <= total:
    print(max(requirements))
    exit()

requirements.sort()

# 상한액 범위 
start = total // region_cnt
# end = sum(requirements) // region_cnt
end = max(requirements)

for i in range(start, end+1):
    idx = bisect_left(requirements, i)
    sum_num = sum(requirements[:idx]) + i * (region_cnt - idx)

    if sum_num <= total:
        answer = i

    else:
        break

print(answer)
