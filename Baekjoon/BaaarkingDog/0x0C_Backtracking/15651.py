# N과 M (3) https://acmicpc.net/problem/15651

"""
자연수 N과 M이 주어졌을 때 아래 조건을 만족하는
길이가 M인 수열을 모두 구하기
- 1부터 N까지 자연수 중 M개를 고른 수열
- 같은 수를 여러 번 골라도 됨 
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
        sol(cur+1)

sol(0)
