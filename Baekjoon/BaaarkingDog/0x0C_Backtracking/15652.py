# N과 M (4) https://acmicpc.net/problem/15652

"""
자연수 N과 M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열 모두 구하기
- 1부터 N까지 자연수 중 M개를 고른 수열
- 같은 수를 여러번 골라도 됨
- 고른 수열은 비내림차순 즉, 오름차순 
--> 길이가 K인 수열 A가 A1<=...<=Ak를 만족 
"""

import sys

n, m = map(int, sys.stdin.readline().split())
answers = [0 for _ in range(m+1)]

def sol(cur):
    global n, m

    if cur == m:
        print(*answers[:m], sep=" ")
        return
    
    for i in range(1, n+1):
        answers[cur] = i

        if answers[cur-1] <= i: # 오름차순으로 만듦
            # cur > 0 조건 안 넣어도 되는 이유는 
            # answers[-1]은 padding 역할을 하고, 항상 0이기 때문 
            sol(cur+1)
        
        
        
sol(0)