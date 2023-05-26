# 용액 https://www.acmicpc.net/problem/2467

"""
산성 용액(양수)과 알칼리성 용액(음수)의 특성값이 정렬된 순서로 주어졌을 때
이 중 두 개의 서로 다른 용액을 혼합해 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액 찾기
"""

import sys

liquid = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

mixed_min = 10 ** 9 * 2 # 최대 10 ** 9 * 2 -1

left, right = 0, liquid - 1
answer = [0, 0]

while left < right:
    mixed = values[left] + values[right]

    if abs(mixed) < mixed_min:
        mixed_min = abs(mixed)
        answer[0], answer[1] = values[left], values[right]

    if mixed > 0:
        right -= 1
    elif mixed < 0:
        left += 1
    else:
        break    


print(*answer)