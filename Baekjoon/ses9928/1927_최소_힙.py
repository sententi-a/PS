# 최소 힙 https://www.acmicpc.net/problem/1927

"""
최소 힙을 이용해 
1. 배열에 자연수 x를 넣는다
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다
위의 두 가지 연산을 지원하는 프로그램 작성하기
"""

import sys 
from heapq import heappop, heappush

nums = []
operation_cnt = int(sys.stdin.readline())

for _ in range(operation_cnt):
    _input = int(sys.stdin.readline())

    # 가장 작은 값을 출력하고, 제거
    if _input == 0:
        if nums:
            print(heappop(nums))
            continue
        print(0)

    # 값을 추가
    else:
        heappush(nums, _input)