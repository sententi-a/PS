# N과 M (5)

"""
자연수 N과 M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열 모두 구하기
N개의 자연수는 모두 다른 수
- 1부터 N까지의 자연수 중 중복 없이 M개를 고른 수열
- 수열은 사전 순으로 증가하는 순서로 출력해야 함 
예) 1 7, 1 8, 1 9, 7 1, 7 8, 7 9...
"""

import sys 

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answers = [0 for _ in range(m+1)]
isused = [False for _ in range(n+1)]

numbers.sort()

def sol(cur):
    global n, m

    if cur == m:
        print(*answers[:m], sep=" ")
        return
    
    for i in range(n):
        if not isused[i]:
            isused[i] = True
            answers[cur] = numbers[i]
            sol(cur+1)
            isused[i] = False

sol(0)