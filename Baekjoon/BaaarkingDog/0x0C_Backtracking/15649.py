# N과 M (1) https://acmicpc.net/problem/15649

"""
자연수 N과 M이 주어졌을 때, 조건 만족하는, 길이가 M인 수열을 모두 구하기
(1 <= M <= N <= 8)
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 

중복되는 수열을 여러 번 출력하면 안 되고, 
각 수열은 공백으로 구분해서 출력
오름차순으로 출력
"""

import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

########1) permutations 써서 해결########
numbers = [i for i in range(1, n+1)]

for case in permutations(numbers, m):
    print(*case, sep=" ")
#######################################

##############2) 재귀 써서 해결#############
nums = [0 for _ in range(m)] # 출력할 값을 담는 리스트
isused = [False for _ in range(n+1)] # 각 값이 사용되었는지 확인 

def sol(k):
    global n, m

    # Base Condition
    if k == m:
        for i in range(m):
            print(nums[i], end=" ")
        print()
        return

    for i in range(1, n+1): 
        # 1부터 n까지의 수 자체가 사용되지 않았다면...
        if not isused[i]:
            nums[k] = i
            isused[i] = 1
            sol(k+1)
            isused[i] = 0

sol(0)
##############################################