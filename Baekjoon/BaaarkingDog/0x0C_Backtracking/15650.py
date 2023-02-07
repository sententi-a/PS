# N과 M (2)

"""
자연수 N과 M이 주어졌을 때, 
조건을 만족하는 길이가 M인 수열 모두 구하기
- 1부터 N까지의 자연수 중 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순 
"""

import sys 

n, m = map(int, sys.stdin.readline().split())
answers = [0 for _ in range(n+1)]
isused = [False for _ in range(n+1)]

def sol(cur):
    global n, m

    if cur == m:
        print(*answers[:m], sep=" ")
    
    for i in range(1, n+1):
        if isused[i]:
            continue
    
        answers[cur] = i
        
        # 중복 체크 로직
        if cur >= 1 and answers[cur] < answers[cur-1]:
            continue
        
        isused[i] = True
        sol(cur+1)
        isused[i] = False

sol(0)